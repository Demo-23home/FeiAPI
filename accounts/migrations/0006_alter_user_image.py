# Generated by Django 5.0.2 on 2024-03-01 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_remove_patientprofile_gender_user_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="profile_pics"),
        ),
    ]