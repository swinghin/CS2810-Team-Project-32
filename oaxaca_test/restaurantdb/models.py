from django.db import models

# Create your models here.


class Employee(models.Model):
    employee_name = models.CharField(max_length=50, default=None)

    def __str__(self):
        return "Employee id:" + str(self.id) + "name:" + str(self.employee_name)
