from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.
class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=10,
                                 choices=[('Waiter', 'Waiter'), ('Kitchen', 'Kitchen')],
                                 default='Kitchen')
