from django.db import models

# Create your models here.

class Allergies(models.Model):
    allergies_id = models.AutoField(primary_key = True)
    allergies_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.allergies_name

