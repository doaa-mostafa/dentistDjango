# Generated by Django 4.1.3 on 2022-12-18 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0005_alter_services_price"),
    ]

    operations = [
        migrations.RenameField(
            model_name="services", old_name="product", new_name="service",
        ),
        migrations.AlterField(
            model_name="services", name="price", field=models.CharField(max_length=50),
        ),
    ]
