# Generated by Django 4.1.3 on 2022-12-27 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0009_rename_name_doctor_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="appoinment", old_name="doctor", new_name="Doctor",
        ),
        migrations.RenameField(
            model_name="appoinment", old_name="patient", new_name="Patient",
        ),
    ]