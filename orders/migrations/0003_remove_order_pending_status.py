# Generated by Django 5.0.2 on 2024-05-16 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_creditcard"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="pending_status",
        ),
    ]