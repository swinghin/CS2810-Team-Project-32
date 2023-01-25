from django.db import models

# Create your models here.

class customer(models.Model):
    name = models.CharField(max_length=80)

class Dish(models.Model):
    Dish_name = models.CharField(max_length=50)
    Dish_id = models.IntegerField(max_length=3)
    Dish_price = models.DecimalField(max_digits=5, decimal_places=2)
