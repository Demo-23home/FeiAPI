# Generated by Django 5.0.2 on 2024-04-30 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doctor", "0007_remove_doctorbooking_pending_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctorbooking",
            name="cancel_reason",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
