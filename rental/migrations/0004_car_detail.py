# Generated by Django 4.2 on 2023-09-07 17:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rental", "0003_alter_car_image_alter_rental_customer_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="detail",
            field=models.CharField(default="", max_length=2000),
        ),
    ]
