# Generated by Django 4.1.3 on 2022-12-27 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0010_rename_doctor_appoinment_doctor_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="appoinment", old_name="date1", new_name="date",
        ),
        migrations.RenameField(
            model_name="appoinment", old_name="time1", new_name="time",
        ),
    ]