from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Dish, Order, Customer


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
        fields = ['order_time', 'order_id', 'dish_id', 'status_id']
        
class TableForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['table_id', 'user', 'total_price', 'persons', 'need_help',]
       
        widgets = {
            'table_id': forms.TextInput(attrs={'class': 'table-cell'}),
            'user': forms.Select(attrs={'class': 'table-cell'}),
            'total_price': forms.NumberInput(attrs={'class': 'table-cell'}),
            'persons': forms.Select(choices=[(1,1)],attrs={'class': 'table-cell'}),
            'need_help': forms.CheckboxInput(attrs={'class': 'form-control-input'}),
        }
    
    def __init__(self, *args, **kwargs):
        maxpersons = kwargs.pop('maxpersons')
        super().__init__(*args, **kwargs)
        numpersons = [(people, people) for people in range(0, maxpersons+1)]
        self.fields['persons'].widget.choices =numpersons
