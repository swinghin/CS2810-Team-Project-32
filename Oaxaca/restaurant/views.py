from django.shortcuts import  render, redirect
from .forms import CreateNewUser
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def redirect_request(request):
    return render(request=request, template_name="home.html")

def register_request(request):
	if request.method == "POST":
		form = CreateNewUser(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("restaurant:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = CreateNewUser()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("http://127.0.0.1:8000/admin/") # change this value if you want to have the login page redirect somwhere.
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})