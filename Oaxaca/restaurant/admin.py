from django.contrib import admin
from .models import *
# register your models here.


admin.site.register(Allergies)
admin.site.register(Ingredient)
admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Customer)
admin.site.register(Status)
admin.site.register(Order)
admin.site.register(Payment)
