# Generated by Django 4.1.3 on 2022-12-27 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0011_rename_date1_appoinment_date_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="doctor", old_name="Name", new_name="doctor_name",
        ),
    ]
