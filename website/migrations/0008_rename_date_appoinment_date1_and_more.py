# Generated by Django 4.1.3 on 2022-12-25 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0007_doctor_patient_appoinment"),
    ]

    operations = [
        migrations.RenameField(
            model_name="appoinment", old_name="date", new_name="date1",
        ),
        migrations.RenameField(
            model_name="appoinment", old_name="time", new_name="time1",
        ),
        migrations.RenameField(model_name="doctor", old_name="Name", new_name="name",),
        migrations.AlterField(
            model_name="patient",
            name="address",
            field=models.CharField(max_length=150),
        ),
    ]
