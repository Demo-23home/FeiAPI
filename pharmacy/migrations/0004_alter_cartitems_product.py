# Generated by Django 5.0.2 on 2024-03-07 22:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pharmacy", "0003_cart_cartitems"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cartitems",
            name="product",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="pharmacy.product",
            ),
            preserve_default=False,
        ),
    ]
