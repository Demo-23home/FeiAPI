# Generated by Django 5.0.2 on 2024-05-21 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("patient", "0003_alter_patientmedicine_plan"),
    ]

    operations = [
        migrations.AddField(
            model_name="patientmedicine",
            name="quantity",
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
