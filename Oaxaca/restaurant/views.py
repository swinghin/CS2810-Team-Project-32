from django.shortcuts import  render, redirect
from .forms import CreateNewUser
from django.contrib.auth import login
from django.contrib import messages

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