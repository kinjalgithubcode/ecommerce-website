from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from .models import Products, Category, Customer
from django.views import View

class Login(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            # flag=check_password(password,customer.password)
            if password == customer.password:
                print("login")
                request.session['customer'] = customer.id
                request.session['email'] = customer.email

                return redirect('homepage')
            else:
                print("NOT LOGIN")
                error_message = 'Invalid Email or Password!!'
        else:
            error_message = 'Invalid Email or Password!!'

        return render(request, 'login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('login')