from django.shortcuts import render

# Create your views here.

def index(request):
    """Home page for the meal_plans app"""
    return render(request, 'meal_plans/index.html')
