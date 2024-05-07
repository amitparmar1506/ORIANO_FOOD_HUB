from django.shortcuts import render,HttpResponse, redirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FoodOrderForm
from .models import FoodOrder

def order_form(request):
    if request.method == 'POST':
        form = FoodOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.total_price = calculate_total_price(order)
            order.save()
            return HttpResponseRedirect('/order-placed/')
    else:
        form = FoodOrderForm()

    return render(request, 'order_form.html', {'form': form})

def calculate_total_price(order):
    
    pizza_price = 99.00
    burger_price = 119.00
    pasta_price = 119.00
    fries_price = 89.00
    cold_drinks_price = 50.00
    sandwich_price = 79.00
    dessert_price = 99.00


    total_price = 0
    total_price += order.pizza_quantity * pizza_price
    total_price += order.burger_quantity * burger_price
    total_price += order.pasta_quantity * pasta_price
    total_price += order.fries_quantity * fries_price
    total_price += order.cold_drinks_quantity * cold_drinks_price
    total_price += order.sandwich_quantity * sandwich_price


    if order.dessert_choice == 'chocolate_softie':
        total_price += order.dessert_quantity * dessert_price
    elif order.dessert_choice == 'vanilla_softie':
        total_price += order.dessert_quantity * dessert_price
    elif order.dessert_choice == 'special_sundae':
        total_price += order.dessert_quantity * dessert_price

    return total_price


def home(request):
    return HttpResponse("Hello! This is my homepage")

def index(request):
    return render(request, 'index.html')

def food(request):
    return render(request,'food delivery.html')

def order_placed(request):
    return render(request, 'order placed.html')

def view_orders(request):
    orders = FoodOrder.objects.all()
    return render(request, 'view orders.html', {'orders': orders})