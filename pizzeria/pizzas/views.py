from django.shortcuts import render

from .models import Pizza

# Create your views here.

def index(request):
    """Home page for the pizzas app"""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """Display all pizzas"""
    pizzas = Pizza.objects.order_by('name')
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    """Display a single pizza and all related toppings"""
    pizza = Pizza.objects.get(id=pizza_id)
    entries = pizza.entry_set.order_by('name')
    context = {'pizza': pizza, 'entries': entries}
    return render(request, 'pizzas/pizza.html', context)