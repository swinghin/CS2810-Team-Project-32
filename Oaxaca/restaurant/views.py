from collections import defaultdict
from django.shortcuts import render

# Create your views here.


def index(request):

    # Temporary hard-coded dish data for use until proper database is completed
    dish_data = [
        [1, "Apple Pie", 0, 3.5, 1200, False, ["DES"], [
            "apple", "butter", "flour", "sugar", "water"]],
        [2, "Bagel", 1, 1.5, 300, True, ["BKY"],
            ["yeast", "flour", "sugar", "salt"]],
        [3, "Baguette", 0, 1, 250, False, ["BKY"], ["apple", "flour", "salt"]],
        [4, "Naked Beans", 0, 2, 500, False, ["BFT", "BEST"], [
            "bean", "tomato", "sugar", "vinegar", "flour", "salt", "spice", "herb"]],
        [5, "Beef Stew", 234, 4, 800, True, ["MAIN"], ["beef", "flour",
                                                       "vinegar", "redwine", "onion", "carrot", "potato", "salt"]],
        [6, "Beef Burger", 0, 3.5, 600, False, ["MAIN"], ["beef", "herb", "onion",
                                                          "egg", "cheese", "tomato", "ketchup", "flour", "yeast", "sugar"]],
        [7, "Biscuits", 0, 1.5, 300, False, ["DES"], [
            "flour", "salt", "sugar", "butter", "milk"]],
        [8, "Blueberry Pie", 0, 3.7, 1150, False, ["DES"], [
            "blueberry", "butter", "flour", "sugar", "water"]],
        [9, "Carrot Cake", 0, 4, 1000, False, ["DES"], [
            "pecan", "sugar", "egg", "applesauce", "flour", "carrot"]],
        [10, "Casserole", 0, 400.5, 1200, False, ["MAIN"], ["beef", "flour",
                                                            "vinegar", "redwine", "onion", "carrot", "potato", "salt"]],
    ]

    dish_list = []
    for i in range(len(dish_data)):
        dish_list.append({
            "dish_id": dish_data[i][0],
            "dish_name": dish_data[i][1],
            "dish_qty": dish_data[i][2],
            "dish_price": dish_data[i][3],
            "dish_cal": dish_data[i][4],
            "dish_avail": dish_data[i][5],
            "dish_cat": dish_data[i][6],
            "dish_ingred": dish_data[i][7],
        })

    dish_categories = {
        "FEAT": "Featured",
        "BEST": "Best Seller",
        "BKY": "Bakery",
        "BFT": "Breakfast",
        "MAIN": "Main",
        "DES": "Dessert",
    }

    dish_by_categories = defaultdict(list)
    for dish in dish_list:
        for category in dish["dish_cat"]:
            dish_by_categories[category].append(
                [dish_categories.get(category), dish])

    dish_by_categories.default_factory = None

    # returns a dictionary of dishes sorted by categories and a dictionary of dish categories
    return render(request, 'restaurant/index.html', {
        "dish_by_categories": dish_by_categories,
        "dish_categories": dish_categories,
    })
