from django.db import models

# Create your models here.


class Employee(models.Model):
    employee_id: models.IntegerField()
    employee_name: models.CharField(max_length=50)

    def __str__(self):
        return "Employee id:" + self.employee_id + "name" + self.employee_name
