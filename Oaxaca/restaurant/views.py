from collections import defaultdict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import CreateNewUser, DishForm, OrderForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.template.loader import render_to_string
from restaurant.models import *


def redirect_request(request):
    return render(request=request, template_name="restaurant/menu_public.html")


def register_request(request):
    if request.method == "POST":
        form = CreateNewUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("restaurant:homepage")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = CreateNewUser()
    return render(request=request, template_name="restaurant/register.html", context={"register_form": form})


def autosearch(request):
    if 'term' in request.GET:
        data = []
        query_set = Dish.objects.filter(
            dish_name__icontains=request.GET.get('term')).order_by('dish_name')
        for result in query_set:
            data = [{'name': result.dish_name}]
        return JsonResponse({'data': data})


def staff_menu(request):
    dish_list = Dish.objects.all().order_by('dish_name').values()
    template = loader.get_template('restaurant/menu_staff.html')
    context = {
        'dish_list': dish_list,
    }
    return HttpResponse(template.render(context, request))


def staff_dish_details(request, id):
    dish = Dish.objects.get(dish_id=id)

    if request.method == 'POST':
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            form.save()
            return redirect('restaurant:staff-menu')
    else:
        template = loader.get_template('restaurant/dish_details.html')
        form = DishForm(instance=dish)
        context = {
            'dish': dish,
            'form': form
        }
    return HttpResponse(template.render(context, request))


def index(request):
    # Get allergen information from DB ordered by allergies_id
    allergens = Allergies.objects.all().order_by('allergies_id').values()

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

    context = {
        "dish_by_categories": dish_by_categories,
        "dish_categories": dish_categories,
        "dish_allergens": dish_allergens,
        "allergens": allergens,
    }

    if request.method == 'POST':
        table_id = request.POST.get('table_id')
        h = HelpNeeded.objects.create(table_id=table_id)

        context['help'] = h

    return render(request, 'restaurant/menu_public.html', context)


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
                # change this value if you want to have the login page redirect somwhere.
                return redirect('restaurant:dashboard')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="restaurant/login.html", context={"login_form": form})

def dashboard(request):
    orders_all = Order.objects.all()
    customer_all = Customer.objects.all()
    help_queryset = customer_all.filter(need_help=True)
    all_helps_needed = HelpNeeded.objects.all()
    context = {
        "orders": orders_all,
        "help": help_queryset,
        "all_helps_needed": all_helps_needed,
    }
    if request.method == "POST":
        help_list = request.POST.getlist("boxes")

        for x in help_list:
            HelpNeeded.objects.filter(id=int(x)).update(helped=True)
        """for x in help_list:
            Customer.objects.filter(pk=int(x)).update(need_help=False)"""
    return render(request, "restaurant/dashboard.html", context=context)
  
def updateOrder(request, pk):
    order = Order.objects.get(order_id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('restaurant:dashboard')
    
    context = {'form':form}
    return render(request, "restaurant/updateOrder.html", context=context)

def cart(request):

    # if request.user.is_authenticated:
    #     customer = request.user.customer
    #     order, created = Order.objects.get_or_create(customer=customer, order_finish=False)
    #     dishes = order.orderitem_set.all()
    # else:
    dishes = []

    context = {'dishes':dishes}
    return render(request, 'restaurant/cart.html', context)


def checkout(request):
    return render(request, 'restaurant/checkout.html')

def ask_waiter(request):
    h = HelpNeeded.objects.create(table_id = 1)

    context = {
        'help': h
    }
    return render(request, 'restaurant/menu_public.html', context)

def kitchen_view(request):
    orders_all = Order.objects.all()
    if request.method == 'POST':
        if request.POST.get("confirm"):
            order_id = int(request.POST.get("confirm"))
            Order.objects.filter(order_id=order_id).update(
                status_id_id=(Status.objects.get(status_name='Cooking').status_id))

        if request.POST.get("cooked"):
            order_id = int(request.POST.get("cooked"))
            Order.objects.filter(order_id=order_id).update(status_id_id=(
                Status.objects.get(status_name='Ready to serve').status_id))
        

    context = {
        "orders": orders_all,
    }
    return render(request, 'restaurant/index_kitchen.html', context)