from django import forms
from django.forms import ModelForm
from .models import Dish

class DishForm(ModelForm):
    class Meta:
        model=Dish
        fields=['dish_name','dish_quantity','dish_price','dish_calories','dish_availability']
        widgets={
            'dish_name':forms.TextInput(attrs={'class':'table-cell'}),
            'dish_quantity':forms.NumberInput(attrs={'class':'table-cell'}),
            'dish_price':forms.NumberInput(attrs={'class':'table-cell'}),
            'dish_calories':forms.NumberInput(attrs={'class':'table-cell'}),
            'dish_availability':forms.CheckboxInput(attrs={'class':'table-cell'}),
        }