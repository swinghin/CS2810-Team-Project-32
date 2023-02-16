from collections import defaultdict
from django.shortcuts import render
from restaurant.models import Allergies, Ingredient, Category, Dish

# Create your views here.


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
