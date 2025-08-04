from django.contrib import admin

from .models import Day
from .models import Meal

admin.site.register(Day)
admin.site.register(Meal)

# Register your models here.