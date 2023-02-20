from django.db import models

# Create your models here.

class Order(models.Model):
    order_id = models.AutoField(primary_key = True)
    order_time = models.TimeField()
    table_id = models.IntegerField()
    order_finish = models.BooleanField()
    dish_id = models.IntegerField()
    status_code = models.CharField(max_length=100)
    class Meta:
        db_table = "Order"

class Allergies(models.Model):
    allergies_id = models.AutoField(primary_key = True)
    allergies_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.allergies_name

class Ingredient(models.Model):
    ingredient_id = models.AutoField(primary_key = True)
    allergies_id = models.ManyToManyField(Allergies)
    ingredient_name = models.CharField(max_length = 20)

    def __str__(self):
        return self.ingredient_name

class Category(models.Model):
    category_id = models.AutoField(primary_key = True)
    category_name = models.CharField(max_length = 20)

    def __str__(self):
        return self.category_name
