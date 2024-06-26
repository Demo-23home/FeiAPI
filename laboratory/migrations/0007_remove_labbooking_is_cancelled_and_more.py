# Generated by Django 5.0.2 on 2024-05-27 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("laboratory", "0006_remove_laboratory_patient"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="labbooking",
            name="is_cancelled",
        ),
        migrations.RemoveField(
            model_name="labbooking",
            name="is_completed",
        ),
        migrations.AddField(
            model_name="labbooking",
            name="status",
            field=models.CharField(
                choices=[
                    ("upcoming", "Upcoming"),
                    ("completed", "Completed"),
                    ("canceled", "Canceled"),
                ],
                default="upcoming",
                max_length=10,
            ),
        ),
    ]
