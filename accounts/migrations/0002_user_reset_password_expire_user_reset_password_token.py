# Generated by Django 5.0.2 on 2024-02-29 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="reset_password_expire",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="reset_password_token",
            field=models.CharField(blank=True, default="", max_length=50),
        ),
    ]
