from django.contrib import admin
from .models import Products
from .models import Category
from .models import Customer
from .models import Order

# Register your models here.

admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
