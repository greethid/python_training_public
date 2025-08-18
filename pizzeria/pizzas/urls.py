"""defines url patterns for pizzas app"""

from django.urls import path

from . import views

app_name = 'pizzas'
urlpatterns = [
    # home page
    path('', views.index, name='index'),
    # Display all pizzas
    path('pizzas/', views.pizzas, name='pizzas'),
    # A detailed page about a single pizza
    path('pizzas/(<int:pizza_id>)', views.pizza, name='pizza'),
]