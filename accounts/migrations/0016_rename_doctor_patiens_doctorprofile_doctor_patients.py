# Generated by Django 5.0.2 on 2024-04-30 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0015_doctorprofile_doctor_patiens"),
    ]

    operations = [
        migrations.RenameField(
            model_name="doctorprofile",
            old_name="doctor_patiens",
            new_name="doctor_patients",
        ),
    ]
