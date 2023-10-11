from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Car(models.Model):
    image = models.ImageField(upload_to='car_images/', default="")
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    detail = models.CharField(max_length=2000, default="")
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(user):
        return user.make
    
    def __str__(user):
        return (
            user.make
            + " "
            + user.model
            + " "
            + str(user.year)
        )

class Rental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    rental_date = models.DateField(default=date.today(), blank=False)
    return_date = models.DateField(blank=True, null=True)

    @property
    def model(user):
        return user.rental_id.model
    
    def __str__(user):
        return (
            user.car.make + " " + user.car.model + " " + str(user.car.year)
            + " was rented by "
            + user.customer.username
            + " on "
            + str(user.rental_date)
        )
    
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(user):
        return f"{user.first_name} - {user.last_name}"

class Categories(models.Model):
    class AudiCar(models.Model):
        image = models.ImageField(upload_to='car_images/Audi/', default="")
        name = models.CharField(max_length=50)
        detail = models.CharField(max_length=1000)
        price = models.DecimalField(max_digits=10, decimal_places=2)

        def __str__(user):
            return user.name

    class BmwCar(models.Model):
        image = models.ImageField(upload_to='car_images/BMW/', default="")
        name = models.CharField(max_length=50)
        detail = models.CharField(max_length=1000)
        price = models.DecimalField(max_digits=10, decimal_places=2)

        def __str__(user):
            return user.name
        
    class MercedesCar(models.Model):
        image = models.ImageField(upload_to='car_images/Mercedes_benz/', default="")
        name = models.CharField(max_length=50)
        detail = models.CharField(max_length=1000)
        price = models.DecimalField(max_digits=10, decimal_places=2)

        def __str__(user):
            return user.name
        
    class ToyotaCar(models.Model):
        image = models.ImageField(upload_to='car_images/Toyota/', default="")
        name = models.CharField(max_length=50)
        detail = models.CharField(max_length=1000)
        price = models.DecimalField(max_digits=10, decimal_places=2)
        
        def __str__(user):
            return user.name
        