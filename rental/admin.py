from django.contrib import admin
from .models import Car, Rental, Categories

# Register your models here.

admin.site.register(Car)
admin.site.register(Categories.AudiCar)
admin.site.register(Categories.BmwCar)
admin.site.register(Categories.MercedesCar)
admin.site.register(Categories.ToyotaCar)
admin.site.register(Rental)
