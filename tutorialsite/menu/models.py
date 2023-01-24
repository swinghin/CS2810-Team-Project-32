from django.db import models

# Create your models here.
class Dishes(models.Model):
    dish_name = models.CharField(max_length=30, default=None)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def __str__(self):
        return self.dish_name + ' ' + self.price
