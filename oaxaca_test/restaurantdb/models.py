from django.db import models

# Create your models here.


class Employee(models.Model):
    employee_name = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.employee_name

class Dish(models.Model):
    dish_name = models.CharField(max_length=50, default=None)
    price = models.DecimalField(max_digits=10,decimal_places=2, default=0.0)

    def __str__(self):
        return self.dish_name

