from django.shortcuts import render, HttpResponse, redirect
from .models import Products
from .models import Category
from .models import Customer
from django.contrib.auth.hashers import check_password

# Create your views here.



def about(request):
    return render(request, 'about.html')




