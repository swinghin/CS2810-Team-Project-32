from collections import defaultdict
from datetime import datetime
from decimal import Decimal
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .forms import CreateNewUser, DishForm, OrderForm, TableForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from django.contrib.auth import logout
from django.template import loader
from django.template.loader import render_to_string
from restaurant.models import *


def redirect_request(request):
    return render(request=request, template_name="restaurant/menu_public.html")


def register_request(request): 
    if request.method == "POST": # Checks if request method is secure POST
        form = CreateNewUser(request.POST)
        if form.is_valid(): # Checks if details entered match requirements
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("restaurant:login") # Redirects user to the login page
        messages.error(
            request, "Unsuccessful registration. Invalid information.") # If details failed to pass requirements, returns this message.
    form = CreateNewUser()
    return render(request=request, template_name="restaurant/register.html", context={"register_form": form})


def logout_request(request):
    logout(request) 
    return render(request=request, template_name="restaurant/logout.html") # Logs user out on button press and temporarily holds them 
                                                                           # at a redirect page.
def autosearch(request):
    if 'term' in request.GET:
        data = []
        query_set = Dish.objects.filter(
            dish_name__icontains=request.GET.get('term')).order_by('dish_name')
        for result in query_set:
            data = [{'name': result.dish_name}]
        return JsonResponse({'data': data})



def index(request):
    """Builds the index (menu) using dish data from the database and renders to browser.

    Args:
        request (HttpRequest): Object containing metadata about the request

    Returns:
        HttpResponse: a rendered HTML page using index template and dish data
    """

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
        # list of all dishes for use in menu.js
        "dish_all": list(dish_all.values()),

        # for rendering menu body
        "dish_by_categories": dish_by_categories,
        "dish_categories": dish_categories,

        # for rendering allergy filter section
        "dish_allergens": dish_allergens,
        "allergens": allergens,
    }

    # If customer presses "need help" button (POST request)
    if request.method == 'POST':
        table_id = request.POST.get('table_id')
        # Get the customer based on table_id and set need_help
        Customer.objects.filter(table_id=table_id).update(need_help=True)
        # for rendering "help is coming" in HTML
        context['help'] = True

    return render(request, 'restaurant/menu_public.html', context)


def payment(request, id):
    customer = Customer.objects.get(table_id=id)
    if request.method == 'POST':
        Payment.objects.create(
            order_id=id, payment_time=datetime.now(), payment_amount=customer.total_price)
        return redirect('restaurant:pay_success', id=id)
    else:
        template = loader.get_template('restaurant/payment.html')
        context = {
            'customer': customer,
            'payment': payment
        }
    return HttpResponse(template.render(context, request))


def payment_success(request, id):
    return HttpResponse(loader.get_template('restaurant/payment_success.html').render({"order_id": id}, request))


def is_waiter(user):
    return user.groups.filter(name='waiter').exists()


def is_kitchen(user):
    return user.groups.filter(name='kitchen').exists()


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username') # takes inputted username
            password = form.cleaned_data.get('password') # takes inputted password
            user = authenticate(username=username, password=password) # checks the details against the database
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                # change this value if you want to have the login page redirect somwhere.
                # if is_waiter(user):
                #     return redirect('restaurant:waiter_page')
                # else:
                return redirect('restaurant:dashboard')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="restaurant/login.html", context={"login_form": form})

def about(request):
    return render(request, "restaurant/aboutpage.html")

@ login_required # added 
def dashboard(request):
    print(" hi", request.user, request.user.groups.all())
    if is_waiter(request.user):
        print("waiter hi")
        return waiter_view(request)
    elif is_kitchen(request.user):
        return kitchen_view(request)
    return redirect('restaurant:login')


def updateOrder(request, pk):
    # form for updating the order clicked in the waiter dashboard.
    order = Order.objects.get(order_id=pk) # selects the order from the pk (primary key) clicked.
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('restaurant:dashboard')

    context = {'form': form}
    return render(request, "restaurant/updateOrder.html", context=context)

def tableManager(request):
    # view for managing table designation.
    context = {
        # list of contexts for individual table objects.
        "One": Customer.objects.get(table_id=1),
        "Two": Customer.objects.get(table_id=2),
        "Three": Customer.objects.get(table_id=3),
        "Four": Customer.objects.get(table_id=4),
        "Five": Customer.objects.get(table_id=5),
        "Six": Customer.objects.get(table_id=6),
        "Seven": Customer.objects.get(table_id=7),
        "Eight": Customer.objects.get(table_id=8),
        "Nine": Customer.objects.get(table_id=9),
        "Ten": Customer.objects.get(table_id=10),
        "Eleven": Customer.objects.get(table_id=11),
        "Twelve": Customer.objects.get(table_id=12)
    }
    return render(request, 'restaurant/tableManager.html', context=context)

def updateTable(request, pk):
    # form for updating the customer data attached to each table currently.
    table = Customer.objects.get(table_id=pk) # selects the table from the pk (primary key) clicked.
    maxpersons = table.maxpersons
    form = TableForm(instance=table,maxpersons=maxpersons)
    if request.method == 'POST':
        form = TableForm(request.POST, instance=table,maxpersons=maxpersons)
        if form.is_valid():
            form.save()
            return redirect('restaurant:tableManager')
    
    context = {
        'form':form,   
    }
    return render(request, "restaurant/updateTable.html", context=context)


def cart(request):
    return render(request, 'restaurant/cart.html', {"dish_all": list(Dish.objects.all().order_by('dish_name').values())})


def orders(request, customer_id):
    customer = Customer.objects.get(table_id=customer_id)
    table_orders = Order.objects.filter(customer=customer)

    orders = []
    for order in table_orders:
        orders.append({
            "order_id": order.order_id,
            "order_time": order.order_time,
            "order_status": Status.objects.get(status_id=order.status_id_id),
            "dishes": order.dish_id.all()
        })

    context = {"orders": orders, "customer": customer}
    return render(request, 'restaurant/orders.html', context)


def checkout(request):
    if request.method == 'POST':
        table_number = request.POST.get("table-number")
        cart_data = request.POST.get("cart-data")
        if table_number and cart_data:
            if not User.objects.filter(username=('waiter'+table_number)).exists():
                print("waiter doesnt exist")
                newWaiter = User.objects.create_user(
                    ('waiter'+table_number), password='password')
                Group.objects.get(name='waiter').user_set.add(newWaiter)
                newWaiter.save()
            if not Customer.objects.filter(table_id=table_number).exists():
                print("customer doesnt exist")
                waiter = User.objects.get(username=('waiter'+table_number))
                newCustomer = Customer(
                    table_id=table_number, total_price=0, persons=0)
                newCustomer.user = waiter
                newCustomer.save()

            customer = Customer.objects.get(table_id=table_number)

            cart_items = []
            cart_total_price = 0
            cart_data = eval(cart_data)
            for dish_id in cart_data:
                dish_count = int(cart_data[dish_id])
                for i in range(dish_count):
                    dish = Dish.objects.get(dish_id=dish_id)
                    cart_items.append(dish)
                    cart_total_price += float(dish.dish_price)

            customer.total_price += customer.total_price + \
                Decimal(cart_total_price)
            customer.save()

            newOrder = Order(order_time=datetime.now(),
                             table_id=table_number,
                             customer=customer,
                             status_id=Status.objects.get(status_name='Order in progress'))
            newOrder.save()
            newOrder.dish_id.set(cart_items)
            # print(newOrder.dish_id.all())
            return redirect('restaurant:pay', id=table_number)

    return render(request, 'restaurant/checkout.html')


@ login_required
@ user_passes_test(is_kitchen, login_url='/login')
def kitchen_view(request):
    #Fetch all orders
    orders_all = Order.objects.all()
    if request.method == 'POST':
        #Checks status of order by first checking the display name of button, in this case confirm being 'recieved'
        if request.POST.get("confirm"):
            #Fetches order id to change status id
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


@ login_required
@ user_passes_test(is_waiter, login_url='/login')
def waiter_view(request):
    #Fetch all orders
    orders = Order.objects.all()
    need_help_tables = Customer.objects.filter(need_help=True)
    context = {
        "orders": orders,
        "need_help_tables": need_help_tables,
    }
    if request.method == "POST":
        # Checks status of order by first checking the display name of button, in this case confirm being 'recieved'
        if request.POST.get("confirm"):
            #Fetches order id to change status id
            order_id = int(request.POST.get("confirm"))
            Order.objects.filter(order_id=order_id).update(
                status_id_id=(Status.objects.get(status_name='Received').status_id))
        
        if request.POST.get("cancel"):
            #Fetches order id to change status id
            order_id = int(request.POST.get("cancel"))
            Order.objects.filter(order_id=order_id).update(
                status_id_id=(Status.objects.get(status_name='Cancelled').status_id))

        if request.POST.get("deliver"):
            order_id = int(request.POST.get("deliver"))
            Order.objects.filter(order_id=order_id).update(status_id_id=(
                Status.objects.get(status_name='Delivered').status_id))
        
        if request.POST.get("helped"):
        #Finds table id that was helped
            helped_table_id = int(request.POST.get("helped"))
            #Removes help request from customer once helped
            Customer.objects.filter(
                table_id=helped_table_id).update(need_help=False)
    return render(request, "restaurant/dashboard.html", context=context)

@ login_required
@ user_passes_test(is_waiter, login_url='/login')
def staff_menu(request):
    """Shows a list of all dishes with edit button for each. Only accessible by waiters.

    Args:
        request (HttpRequest): Object containing metadata about the request

    Returns:
        HttpResponse: a rendered HTML page of list of dishes
    """

    # Get all dishes and order by dish name
    dish_list = Dish.objects.all().order_by('dish_name').values()
    template = loader.get_template('restaurant/menu_staff.html')
    context = {
        'dish_list': dish_list,
    }
    return HttpResponse(template.render(context, request))


@ login_required
@ user_passes_test(is_waiter, login_url='/login')
def staff_dish_details(request, id):
    """Shows an editing form for a dish by id. Only accessible by waiters.

    Args:
        request (HttpRequest): Object containing metadata about the request
        id (int): the dish id for lookup

    Returns:
        HttpResponse: a rendered HTML page using dish details template and dish data by id
    """

    # Get dish by id
    dish = Dish.objects.get(dish_id=id)

    # If POST request, save dish data and redirect to staff menu
    if request.method == 'POST':
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            form.save()
            return redirect('restaurant:staff-menu')

    # If not POST request or form invalid, show dish form
    template = loader.get_template('restaurant/dish_details.html')
    form = DishForm(instance=dish)
    context = {
        'dish': dish,
        'form': form
    }

    return HttpResponse(template.render(context, request))
