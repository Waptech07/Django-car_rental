# Generated by Django 4.2 on 2023-09-07 16:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rental", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="image",
            field=models.ImageField(default="", upload_to="car_images/"),
        ),
    ]
