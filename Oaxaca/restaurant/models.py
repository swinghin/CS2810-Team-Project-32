from django.db import models
from array import array

# Create your models here.

class Allergies(models.Model):
    allergies_id = models.AutoField(primary_key = True)
    allergies_name = models.CharField(max_length = 50)

    def __str__(self):
        return str(self.allergies_name)

class Ingredient(models.Model):
    ingredient_id = models.AutoField(primary_key = True)
    allergies_id = models.ManyToManyField(Allergies)
    ingredient_name = models.CharField(max_length = 20)

    def __str__(self):
        return str(self.ingredient_name)

class Category(models.Model):
    category_id = models.AutoField(primary_key = True)
    category_name = models.CharField(max_length = 20)

    def __str__(self):
        return str(self.category_name)

class Dish(models.Model):
    dish_id = models.AutoField(primary_key = True)
    dish_name = models.CharField(max_length = 75)
    dish_quantity = models.IntegerField()
    dish_price = models.DecimalField(max_digits=7, decimal_places=2)
    dish_calories = models.IntegerField()
    dish_availability = models.BooleanField(default = False)

    ingredient_id = models.ManyToManyField(Ingredient)
    category_id = models.ManyToManyField(Category)

    def __str__(self):
        return str(self.dish_name)

class Customer(models.Model):
    table_id = models.AutoField(primary_key = True)
    total_price = models.DecimalField(max_digits=11, decimal_places=2)
    persons = models.IntegerField()
    need_help = models.BooleanField(default = False)

    def __str__(self):
        return str(self.table_id)
"""
class Status(models.Model):
    class Statuses(models.TextChoices):
        InProgress = 'Order in progress'
        Received = 'Received'
        Cooking = 'Cooking'
        Problem = 'Problem'
        Ready = 'Ready'
    
    status_id = models.AutoField(primary_key = True)
    status_name = models.CharField(max_length = 20, choices=Statuses.choices, default=Statuses.InProgress)

    def __str__(self):
        return str(self.status_name)
"""
class Order(models.Model):
    statuses = [('order_in_progress','Order in progress'), ('received','Received'), ('cooking','Cooking'), ('problem','Problem'), ('ready','Ready')]
    order_id = models.AutoField(primary_key = True)
    order_time = models.DateTimeField()
    table_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_finish = models.BooleanField(default = False)
    dish_id = models.ManyToManyField(Dish)
    status = models.CharField(max_length = 20, choices=statuses, default=statuses[0])

    def __str__(self):
        return "Order no: " + str(self.order_id)
