# Generated by Django 4.1.3 on 2022-12-15 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0003_rename_service_service_product"),
    ]

    operations = [
        migrations.RenameModel(old_name="Service", new_name="Services",),
    ]
