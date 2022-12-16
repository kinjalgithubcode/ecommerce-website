from django.shortcuts import render, HttpResponse, redirect
from .models import Customer
from django.contrib.auth.hashers import check_password
from django.views import View

class SignUp(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        c1 = Customer(fname=fname, lname=lname, phone=phone, email=email, password=password)
        c1.save()
        return render(request, 'index.html')
        return HttpResponse(' Inserted Successfully :)')

