from django.db import models
from django.conf import settings
from pharmacy.models import Product
from accounts.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator

from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


class CreditCard(models.Model):
    MASTER_CARD = "MasterCard"
    VISA = "VISA"
    AMERICAN_EXPRESS = "American Express"

    CARD_TYPE_CHOICES = [
        (MASTER_CARD, "MasterCard"),
        (VISA, "Visa"),
        (AMERICAN_EXPRESS, "American Express"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_number = models.CharField(
        max_length=16, validators=[MinLengthValidator(16), MaxLengthValidator(16)]
    )
    expiration_date = models.CharField(
        max_length=5
    )  # Consider adding validation for date format (MM/YY)
    cvv = models.CharField(
        max_length=3, validators=[MinLengthValidator(3), MaxLengthValidator(3)]
    )
    card_type = models.CharField(max_length=16, choices=CARD_TYPE_CHOICES)

    def __str__(self):
        return f"Card ending with {self.card_number[-4:]} for user {self.user}"

    class Meta:
        verbose_name = "Credit Card"
        verbose_name_plural = "Credit Cards"


class Order(models.Model):
    PAYMENT_STATUS_PENDING = "P"
    PAYMENT_STATUS_COMPLETE = "C"
    PAYMENT_STATUS_FAILED = "F"

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, "Pending"),
        (PAYMENT_STATUS_COMPLETE, "Complete"),
        (PAYMENT_STATUS_FAILED, "Failed"),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    pending_status = models.CharField(
        max_length=50, choices=PAYMENT_STATUS_CHOICES, default="PAYMENT_STATUS_PENDING"
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return self.pending_status

    @property
    def total_price(self):
        items = self.items.all()
        total = sum([item.quantity * item.product.price for item in items])
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.product.name
