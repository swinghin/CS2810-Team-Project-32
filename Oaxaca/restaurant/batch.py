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
        "Drinks",
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
        ["Scallops", "Crustacean"],
        ["Cauliflower", ""],
        ["Oil", ""],
        ["Weed", ""],
        ["Scalops", "Crustacean"],
        ["Dates", "Nuts"],
        ["Pepper", ""],
        ["Pseudoephedrine", ""],
        ["Strawberry", ""],
        ["Uranium-238", ""],
        ["Lamb", ""],
        ["Lobster", "Crustacean"],
        ["Clams", "Crustacean"],
        ["Stock", ""],
        ["Jelly", ""],
        ["Fat", ""],
        ["Garlic", ""],
        ["Oats", "Gluten"],
        ["Coffee Beans", ""],
        ["Cabbage", ""],
        ["Pork", ""],
        ["Chickpeas", ""],
        ["Baking Powder", ""],
        ["Yogurt", "Milk"],
        ["Honey", ""],
        ["Pumpkin Seeds", ""],
        ["Sunflower Seeds", ""],
        ["Sesame Seeds", ""],
        ["Almonds", "Nuts"],
        ["Dried Berries", ""],
        ["Coconut", ""],
        ["Sausage", ""],
        ["Mustard", ""],
        ["Mayo", ""],
        ["Bacon", ""],
        ["Double Cream", ""],
        ["Fart", ""],
        ["Pineapple", ""],
        ["Bread", "Gluten"],
    ]
    for ingred_allerg in ingredient_sheet:
        ingred = Ingredient(ingredient_name=ingred_allerg[0])
        ingred.save()
        if (ingred_allerg[1]):
            ingred.allergies_id.set(
                [Allergies.objects.get(allergies_name=ingred_allerg[1])])


def add_dishes():
    dish_sheet = [
        ["Apple Pie", 65, 3.5, 1200, True, ["Desserts"], [
            "Apple", "Butter", "Flour", "Sugar", "Water"]],
        ["Bagel", 71, 1.5, 300, True, ["Bakery"],
            ["Yeast", "Flour", "Sugar", "Salt"]],
        ["Baguette", 69, 1, 250, True, ["Bakery"], ["Apple", "Flour", "Salt"]],
        ["Naked Beans", 16, 2, 500, True, ["Breakfast", "Best Sellers"], [
            "Bean", "Tomato", "Sugar", "Vinegar", "Flour", "Salt", "Spice", "Herb"]],
        ["Beef Stew", 54, 4, 800, True, ["Main Dishes"], ["Beef", "Flour",
                                                          "Vinegar", "Red Wine", "Onion", "Carrot", "Potato", "Salt"]],
        ["Beef Burger", 9, 3.5, 600, True, ["Main Dishes"], ["Beef", "Herb",
                                                             "Onion", "Egg", "Cheese", "Tomato", "Ketchup", "Flour", "Yeast", "Sugar"]],
        ["Biscuits", 10, 1.5, 300, True, ["Desserts", "Sides"],
            ["Flour", "Salt", "Sugar", "Butter", "Milk"]],
        ["Blueberry Pie", 40, 3.7, 1150, True, ["Desserts"], [
            "Blueberry", "Butter", "Flour", "Sugar", "Water"]],
        ["Breast Milk", 82, 0, 2500, True, ["Breakfast", "Best Sellers"], ["Milk"]],
        ["Carrot Cake", 90, 4, 1000, True, ["Desserts"], [
            "Pecan", "Sugar", "Egg", "Applesauce", "Flour", "Carrot"]],
        ["Cauliflower Cheese", 13, 3.5, 900, True,
            ["Sides"], ["Cauliflower", "Cheese"]],
        ["Casserole", 12, 400.5, 1200, True, ["Main Dishes"], [
            "Beef", "Flour", "Vinegar", "Red Wine", "Onion", "Carrot", "Potato", "Salt"]],
        ["Cheeseburger", 58, 5, 1420, True, ["Main Dishes"], ["Beef", "Flour",
                                                              "Yeast", "Water", "Sugar", "Cheese", "Salt", "Pepper", "Bread"]],
        ["Clams", 19, 1, 400, True, ["Sides"], ["Clams"]],
        ["Covfefe", 22, 2.5, 300, True, ["Drinks"], ["Coffee Beans"]],
        ["Dates", 65, 0.5, 50, True, ["Desserts"], ["Dates"]],
        ["Davey's Gravy", 70, 2, 270, True, ["Main Dishes", "Featured"],
            ["Stock", "Flour", "Butter", "Jelly"]],
        ["Dirty Dumplings", 28, 0.01, 2500, True, ["Sides"], ["Fat", "Flour"]],
        ["Doner Kebab", 10, 3, 670, True, ["Main Dishes"], ["Lamb", "Onion",
                                                            "Garlic", "Flour", "Oil", "Cabbage", "Tomato", "Water", "Yeast"]],
        ["English Muffins", 23, 10, 420, True, ["Desserts"], [
            "Flour", "Yeast", "Salt", "Milk", "Water", "Butter"]],
        ["Eggrolls", 78, 2, 300, True, ["Sides"], [
            "Egg", "Pork", "Cabbage", "Carrot", "Water", "Flour", "Oil"]],
        ["Falafel & Hummus", 75, 1.5, 545, True, ["Main Dishes"], [
            "Chickpeas", "Baking Powder", "Onion", "Garlic", "Salt", "Pepper"]],
        ["French Fries", 33, 1, 230, True, ["Sides"], ["Potato", "Salt", "Oil"]],
        ["Garlic Bread", 21, 2, 300, True, ["Sides"], [
            "Flour", "Salt", "Yeast", "Water", "Garlic", "Butter"]],
        ["Granola & Yogurt", 66, 1.5, 495, True, ["Desserts"], ["Yogurt", "Coconut",
                                                                "Sesame Seeds", "Sunflower Seeds", "Pumpkin Seeds", "Oil", "Honey"]],
        ["Gutins Pudding", 87, 25, 1000, True, ["Sides", "Featured"], ["Sugar"]],
        ["Hamburger", 56, 4, 300, True, ["Main Dishes"], [
            "Beef", "Flour", "Salt", "Water", "Yeast", "Pepper"]],
        ["Hash Brown", 69, 2, 330, True, ["Sides"], ["Potato", "Butter"]],
        ["Snoop Hot Dogg", 5, 1.5, 420, True, ["Main Dishes"], ["Weed", "Sausage",
                                                                "Ketchup", "Mustard", "Butter", "Bacon", "Flour", "Yeast", "Water", "Salt"]],
        ["Ice Cream", 54, 1, 200, True, ["Desserts"],
            ["Double Cream", "Sugar", "Egg", "Milk"]],
        ["Jam Donut", 82, 1, 300, True, ["Desserts"], [
            "Sugar", "Strawberry", "Yeast", "Flour", "Butter", "Water"]],
        ["Jasper's Jelly", 57, 25, 60, True, [
            "Desserts", "Featured"], ["Jelly", "Sugar", "Water"]],
        ["Kebab Salad", 46, 2.5, 400, True, ["Main Dishes"], ["Cabbage"]],
        ["Kidney Beans", 96, 1, 330, True, ["Breakfast"], ["Bean"]],
        ["Lasagna", 55, 5, 135, True, ["Main Dishes"], ["Beef", "Flour", "Egg",
                                                        "Water", "Butter", "Tomato", "Cheese", "Garlic", "Red Wine", "Carrot"]],
        ["Lambsticks", 26, 6, 300, True, ["Main Dishes"],
            ["Lamb", "Garlic", "Oil", "Salt", "Pepper"]],
        ["Lobster Stew", 74, 2, 310, True, ["Main Dishes"], [
            "Lobster", "Garlic", "Milk", "Butter", "Salt", "Double Cream"]],
        ["Margherita Pizza", 74, 5.5, 266, True, ["Main Dishes"], [
            "Flour", "Salt", "Yeast", "Water", "Tomato", "Oil", "Cheese", "Salt"]],
        ["Methane Gas", 37, 2147, 3000, True, [
            "Breakfast", "Best Sellers"], ["Fart"]],
        ["Meth", 73, 0, 420, True, ["Desserts"], ["Pseudoephedrine"]],
        ["Mom's Spaghetti", 82, 20.02, 624, True, ["Main Dishes", "Featured"],
            ["Tomato", "Onion", "Carrot", "Celery", "Garlic", "Flour", "Egg"]],
        ["Noodles", 53, 4, 138, True, ["Main Dishes"],
            ["Flour", "Yeast", "Egg", "Water"]],
        ["Pancakes", 50, 5, 227, True, ["Breakfast"],
            ["Flour", "Oil", "Milk", "Egg", "Sugar"]],
        ["Pepper Sprinkles", 44, 2, 6, True, ["Sides"], ["Pepper"]],
        ["Pineapple Pizza", 59, 10, 244, True, ["Main Dishes"], [
            "Yeast", "Flour", "Water", "Tomato", "Salt", "Cheese", "Oil", "Pineapple"]],
        ["Sigma Meat Balls", 61, 6, 669, True, [
            "Desserts", "Best Sellers"], ["Beef"]],
        ["Strawberry Milkshake", 90, 5, 235, True, ["Drinks"],
            ["Strawberry", "Milk", "Double Cream", "Sugar"]],
        ["Tater Tots", 81, 3, 212, True, ["Sides"], [
            "Potato", "Pepper", "Cheese", "Onion"]],
        ["Trollope's Scallops", 1, 30, 94, True, [
            "Main Dishes", "Featured"], ["Scallops", "Oil"]],
        ["Uranium", 28, 130, 18000000, True, [
            "Main Dishes", "Best Sellers"], ["Uranium-238"]],
        ["Waffle House", 39, 2000, 291, True, ["Main Dishes"],
            ["Yeast", "Flour", "Water", "Sugar"]],
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
