# Generated by Django 4.2 on 2023-09-13 20:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("rental", "0007_remove_audi_car_image_remove_bmw_car_image_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="AUDI",
            new_name="AUDI_CAR",
        ),
        migrations.RenameModel(
            old_name="BMW",
            new_name="BMW_CAR",
        ),
        migrations.RenameModel(
            old_name="TOYOTA",
            new_name="TOYOTA_CAR",
        ),
    ]
