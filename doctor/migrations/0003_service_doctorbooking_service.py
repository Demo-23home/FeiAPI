# Generated by Django 5.0.2 on 2024-04-05 20:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doctor", "0002_remove_doctorbooking_duration_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "service",
                    models.CharField(
                        choices=[
                            ("Standard Appointment", "Standard Appointment"),
                            ("Specialist Consultations", "Specialist Consultations"),
                            ("follow-up appointment", "follow-up appointment"),
                        ],
                        max_length=50,
                    ),
                ),
                ("price", models.PositiveBigIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name="doctorbooking",
            name="service",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="doctor.service",
            ),
            preserve_default=False,
        ),
    ]