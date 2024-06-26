from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator
from django.apps import apps


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        PATIENT = "PATIENT", "Patient"
        DOCTOR = "DOCTOR", "Doctor"

    role = models.CharField(choices=Role.choices, max_length=10, default=Role.PATIENT)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(unique=True)
    image = models.ImageField(
        null=True, blank=True, upload_to="profile_pics", default="user-avatar.png"
    )

    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
    )
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, null=True, blank=True
    )
    reset_password_token = models.CharField(max_length=50, default="", blank=True)
    reset_password_expire = models.DateTimeField(null=True, blank=True)

    CITY_CHOICES = (
        ("MANS", "Mansoura"),
        ("NDAM", "New-Dammitta"),
        ("CAI", "Cairo"),
    )
    city = models.CharField(max_length=100, choices=CITY_CHOICES, null=True, blank=True)
    GOVERNMENT_CHOICES = (
        ("DAKH", "Dakhlia"),
        ("DAMI", "Dammitta"),
        ("CAI", "Cairo"),
    )
    government = models.CharField(
        max_length=100, choices=GOVERNMENT_CHOICES, null=True, blank=True
    )

    birth_date = models.DateField(null=True, blank=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    def __str__(self):
        return self.username


class PatientProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="patient_profile"
    )

    def __str__(self):
        return f"{self.user.username}'s Patient Profile"


SPECIALIZATION = (
    ("CARDIOLOGIST", "cardiologist"),
    ("Neurologist", "Neurologist"),
    ("Pulmonologist", "Pulmonologist"),
)


class DoctorProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="doctor_profile"
    )
    bio = models.TextField(null=True, blank=True)
    verified = models.BooleanField(default=False)
    rating = models.IntegerField(
        null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    experience = models.PositiveIntegerField(null=True, blank=True)
    doctor_patients = models.PositiveBigIntegerField(null=True, blank=True)
    specialization = models.CharField(max_length=50, choices=SPECIALIZATION)

    def update_average_rating(self):
        DoctorBooking = apps.get_model("doctor", "DoctorBooking")
        average_rating = DoctorBooking.objects.filter(
            doctor=self.user, rating__isnull=False
        ).aggregate(models.Avg("rating"))["rating__avg"]
        self.rating = average_rating
        self.save()

    def __str__(self):
        return f"{self.user.username}'s Doctor Profile"


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == User.Role.PATIENT:
            PatientProfile.objects.create(user=instance)
        elif instance.role == User.Role.DOCTOR:
            DoctorProfile.objects.create(user=instance)
