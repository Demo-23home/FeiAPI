# Generated by Django 5.0.2 on 2024-04-08 15:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doctor", "0005_rename_booking_hour_doctorbooking_booking_date_and_more"),
        ("orders", "0002_creditcard"),
    ]

    operations = [
        migrations.AddField(
            model_name="doctorbooking",
            name="cancel_reason",
            field=models.CharField(default="", max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="doctorbooking",
            name="is_cancelled",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="doctorbooking",
            name="payment_card",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="orders.creditcard",
            ),
        ),
        migrations.AddField(
            model_name="doctorbooking",
            name="pending_status",
            field=models.CharField(
                choices=[("P", "Pending"), ("C", "Complete"), ("F", "Failed")],
                default="PAYMENT_STATUS_PENDING",
                max_length=50,
            ),
        ),
    ]