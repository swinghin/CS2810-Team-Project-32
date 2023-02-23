from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Dish, Order


# Create your forms here.

class CreateNewUser(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def save(self, commit=True):
        user = super(CreateNewUser, self).save(commit=False)
        if commit:
            user.save()
        return user


class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = ['dish_name', 'dish_quantity', 'dish_price',
                  'dish_calories', 'dish_availability']
        widgets = {
            'dish_name': forms.TextInput(attrs={'class': 'table-cell'}),
            'dish_quantity': forms.NumberInput(attrs={'class': 'table-cell'}),
            'dish_price': forms.NumberInput(attrs={'class': 'table-cell'}),
            'dish_calories': forms.NumberInput(attrs={'class': 'table-cell'}),
            'dish_availability': forms.CheckboxInput(attrs={'class': 'slide-toggle-checkbox'}),
        }

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'