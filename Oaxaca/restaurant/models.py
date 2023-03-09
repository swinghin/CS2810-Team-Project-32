from django.db import models
from array import array
from django.contrib.auth.models import User
# Create your models here.


class Allergies(models.Model):
    allergies_id = models.AutoField(primary_key=True)
    allergies_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.allergies_name)
        return str(self.allergies_name)


class Ingredient(models.Model):
    ingredient_id = models.AutoField(primary_key=True)
    allergies_id = models.ManyToManyField(Allergies)
    ingredient_name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.ingredient_name)
        return str(self.ingredient_name)


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.category_name)


class Dish(models.Model):
    dish_id = models.AutoField(primary_key=True)
    dish_name = models.CharField(max_length=75)
    dish_quantity = models.IntegerField()
    dish_price = models.DecimalField(max_digits=7, decimal_places=2)
    dish_calories = models.IntegerField()
    dish_availability = models.BooleanField(default=False)

    ingredient_id = models.ManyToManyField(Ingredient)
    category_id = models.ManyToManyField(Category)

    def __str__(self):
        return str(self.dish_name)


class Customer(models.Model):
    table_id = models.AutoField(primary_key = True)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=11, decimal_places=2)
    persons = models.IntegerField()
    need_help = models.BooleanField(default=False)

    def __str__(self):
        return str(self.table_id)


class Status(models.Model):
    class Statuses(models.TextChoices):
        InProgress = 'Order in progress'
        Received = 'Received'
        Cooking = 'Cooking'
        Ready = 'Ready to serve'
        Delivered = 'Delivered'
        Problem = 'Problem'
        Cancelled = 'Cancelled'

    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(
        max_length=20, choices=Statuses.choices, default=Statuses.InProgress)

    def __str__(self):
        return str(self.status_name)


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_time = models.DateTimeField()
    table_id = models.IntegerField()
    customer = models.ForeignKey(Customer, null=True, to_field='user', on_delete=models.CASCADE)
    order_finish = models.BooleanField(default = False)
    dish_id = models.ManyToManyField(Dish)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return "Order no: " + str(self.order_id)
    
class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    payment_time = models.DateTimeField()
    payment_amount = models.DecimalField(max_digits=7, decimal_places=2)
     
    def __str__(self):
        return "Order no: " + str(self.order_id) + "Amount: " + str(self.payment_amount)
