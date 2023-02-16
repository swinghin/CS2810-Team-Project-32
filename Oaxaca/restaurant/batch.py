from restaurant.models import Allergies, Ingredient, Category, Dish


def add_allergies():
    allergen_sheet = [
        "Celery",
        "Gluten",
        "Crustacean",
        "Mustard",
        "Peanuts",
        "Sesame",
        "Soy",
        "Sulphite",
        "Nuts",
        "Milk",
        "Egg",
    ]
    for allergen in allergen_sheet:
        Allergies.objects.create(allergies_name=allergen)


def add_categories():
    categories_sheet = [
        "Featured",
        "Best Sellers",
        "Main Dishes",
        "Sides",
        "Desserts",
        "Breakfast",
        "Bakery",
    ]
    for category in categories_sheet:
        Category.objects.create(category_name=category)


def add_ingredients():
    ingredient_sheet = [
        ["Celery", "Celery"],
        ["Yeast", "Gluten"],
        ["Flour", "Gluten"],
        ["Apple", ""],
        ["Butter", ""],
        ["Sugar", ""],
        ["Water", ""],
        ["Salt", ""],
        ["Bean", ""],
        ["Tomato", ""],
        ["Vinegar", ""],
        ["Spice", ""],
        ["Herb", ""],
        ["Beef", ""],
        ["Red Wine", ""],
        ["Onion", ""],
        ["Carrot", ""],
        ["Potato", ""],
        ["Egg", "Egg"],
        ["Cheese", "Milk"],
        ["Ketchup", ""],
        ["Milk", "Milk"],
        ["Blueberry", ""],
        ["Applesauce", ""],
        ["Pecan", "Nuts"],
    ]
    for ingred_allerg in ingredient_sheet:
        ingred = Ingredient(ingredient_name=ingred_allerg[0])
        ingred.save()
        if (ingred_allerg[1]):
            ingred.allergies_id.set(
                [Allergies.objects.get(allergies_name=ingred_allerg[1])])


def add_dishes():
    dish_sheet = [
        ["Apple Pie", 0, 3.5, 1200, False, ["Desserts"], [
            "Apple", "Butter", "Flour", "Sugar", "Water"]],
        ["Bagel", 1, 1.5, 300, True, ["Bakery"],
            ["Yeast", "Flour", "Sugar", "Salt"]],
        ["Baguette", 0, 1, 250, False, ["Bakery"], ["Apple", "Flour", "Salt"]],
        ["Naked Beans", 0, 2, 500, False, ["Breakfast", "Best Sellers"], [
            "Bean", "Tomato", "Sugar", "Vinegar", "Flour", "Salt", "Spice", "Herb"]],
        ["Beef Stew", 234, 4, 800, True, ["Main Dishes"], ["Beef", "Flour",
                                                           "Vinegar", "Red Wine", "Onion", "Carrot", "Potato", "Salt"]],
        ["Beef Burger", 0, 3.5, 600, False, ["Main Dishes"], ["Beef", "Herb",
                                                              "Onion", "Egg", "Cheese", "Tomato", "Ketchup", "Flour", "Yeast", "Sugar"]],
        ["Biscuits", 0, 1.5, 300, False, ["Desserts", "Sides"],
            ["Flour", "Salt", "Sugar", "Butter", "Milk"]],
        ["Blueberry Pie", 0, 3.7, 1150, False, ["Desserts"], [
            "Blueberry", "Butter", "Flour", "Sugar", "Water"]],
        ["Breast Milk", 45, 0, 2500, True, ["Breakfast", "Best Sellers"], ["Milk"]],
        ["Carrot Cake", 0, 4, 1000, False, ["Desserts"], [
            "Pecan", "Sugar", "Egg", "Applesauce", "Flour", "Carrot"]],
    ]

    for i in range(len(dish_sheet)):
        current_dish = dish_sheet[i]
        dish = Dish(
            dish_name=current_dish[0],
            dish_quantity=current_dish[1],
            dish_price=current_dish[2],
            dish_calories=current_dish[3],
            dish_availability=current_dish[4],
        )
        dish.save()

        dish_categories = current_dish[5]
        dish_category_ids = []
        for j in range(len(dish_categories)):
            dish_category_ids.append(Category.objects.get(
                category_name=dish_categories[j]))
        dish.category_id.set(dish_category_ids)

        dish_ingredients = current_dish[6]
        dish_ingredient_ids = []
        for k in range(len(dish_ingredients)):
            dish_ingredient_ids.append(Ingredient.objects.get(
                ingredient_name=dish_ingredients[k]))
        dish.ingredient_id.set(dish_ingredient_ids)


def add_all():
    add_allergies()
    add_ingredients()
    add_categories()
    add_dishes()


def drop_all():
    Dish.objects.all().delete()
    Category.objects.all().delete()
    Ingredient.objects.all().delete()
    Allergies.objects.all().delete()
