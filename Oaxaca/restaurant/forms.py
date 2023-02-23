from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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