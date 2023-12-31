# Generated by Django 4.2 on 2023-09-13 19:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rental", "0005_user_alter_car_image_alter_rental_rental_date_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="AUDI",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("car_image", models.ImageField(default="", upload_to="BMW/")),
                ("name", models.CharField(max_length=20)),
                ("detail", models.CharField(max_length=1000)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="BMW",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("car_image", models.ImageField(default="", upload_to="BMW/")),
                ("name", models.CharField(max_length=20)),
                ("detail", models.CharField(max_length=1000)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Categories",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TOYOTA",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("car_image", models.ImageField(default="", upload_to="BMW/")),
                ("name", models.CharField(max_length=20)),
                ("detail", models.CharField(max_length=1000)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AlterField(
            model_name="rental",
            name="rental_date",
            field=models.DateField(default=datetime.date(2023, 9, 13)),
        ),
    ]
