"""Defines url patterns for users app"""

from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # Including default authentication urls
    path('', include('django.contrib.auth.urls')),
]

