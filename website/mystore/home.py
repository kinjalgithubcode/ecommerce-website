from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from .models import Products, Category, Customer
from django.views import View


class Index(View):

    def post(self,request):
        product = request.POST.get('product')#id
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart [product] = quantity - 1
                else:
                    cart [product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart    # creating session cart variable
        print('cart',request.session['cart'])
        return redirect('homepage')


    def get(self,request):
        return HttpResponseRedirect(f'/mystore{request.get_full_path()[1:]}')



def mystore(request):
    cart=request.session.get('cart')
    if not cart:
        request.session['cart']={}

    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)

    else:
        products = Products.get_all_products()
    # products=Products.get_all_products()

    data = {}
    data['products'] = products
    data['categories'] = categories
    print(products)
    print('i am ', request.session.get('email'))

    print('my id is ', request.session.get('customer'))

    return render(request, 'index.html', data)


