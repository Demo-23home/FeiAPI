# Generated by Django 5.0.2 on 2024-05-18 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doctor", "0010_doctorbooking_review"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctorbooking",
            name="review",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
