from collections import defaultdict
from django.http import HttpResponse
from django.shortcuts import  render, redirect
from .forms import CreateNewUser
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.template import loader
from restaurant.models import Allergies, Ingredient, Category, Dish

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


def index(request):
    # Get allergen information from DB ordered by allergies_id
    allergens = Allergies.objects.all().order_by('allergies_id').values()

    # Get ingredients info from DB
    # ingredients=Ingredient.objects.all()
    # allergic_ingredient_ids=[]
    # for ingredient in ingredients.values():
    #     if ingredient['allergies_id']:
    #         allergic_ingredient_ids.append(ingredient['ingredient_id'])
    # print(allergic_ingredient_ids)

    # Get dish categories from DB
    dish_categories = Category.objects.values()

    # Get all dishes from DB ordered by dish name
    dish_all = Dish.objects.all().order_by('dish_name')

    # Create a dictionary of lists to store dishes based on category
    dish_by_categories = defaultdict(list)
    dish_by_categories.default_factory = None
    # Pre-fill categories to dictionary
    for category in dish_categories:
        dish_by_categories[category['category_name']] = []

    # Create list for filtering with JS
    dish_allergens = []

    # Loop though all dishes
    for dish in dish_all:
        # To store allergens of each dish
        dish_allergen_list = []
        # Loop though ingredients of the dish
        for dish_ingred in dish.ingredient_id.all():
            # If there are allergic dishes, append all allergens to dish_allergen_list
            if dish_ingred.allergies_id.values():
                for allergen in dish_ingred.allergies_id.values():
                    dish_allergen_list.append(allergen['allergies_name'])
        # Append allergen info to dish_allergens list for use in filtering
        dish_allergens.append({
            "dish_id": dish.dish_id, 
            "dish_allergen_list": dish_allergen_list
        })

        # loop though the categories of the dish and add it to dish_by_categories based on thecategory
        for dish_category in dish.category_id.values():
            dish_by_categories[dish_category['category_name']].append(dish)

    return render(request, 'restaurant/index.html', {
        "dish_by_categories": dish_by_categories,
        "dish_categories": dish_categories,
        "dish_allergens": dish_allergens,
        "allergens": allergens,
    })

def payment(request):
    template = loader.get_template('restaurant/payment.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
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