from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class createNewUser(UserCreationForm):

    username = forms.RegexField(required=True)
    password1 = forms.RegexField(required=True)
    password2 = forms.RegexField(required=True)
    
    class Meta: 
        model = User
        fields = ("username", "password1", "password2")

    
    def save(self, commit=True):
        return super().save(commit)