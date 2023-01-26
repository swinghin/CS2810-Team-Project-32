from django.db import models
class Dishes(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()

class Drinks(models.Model):
    name = models.CharField(max_length=80)
    cost = models.IntegerField()
    size = models.CharField(max_length=80)
   