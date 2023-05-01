from itertools import product
from django import views
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from .models import Product
from .models import Category
from .models import Customer
from .models import Order, Contact
from .auth import auth_middleware
from django.utils.decorators import method_decorator


# Create your views here.
class Index(View):

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print('Your cart is', request.session['cart'])

        return redirect('homepage')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        product = None
        category = Category.objects.all
        categoryID = request.GET.get('category')
        if categoryID:
            product = Product.get_all_prodect_by_category_id(categoryID)
        else:
            product = Product.objects.all
        data = {}
        data['product'] = product
        data['category'] = category
        print('You are:', request.session.get('email'))
        return render(request, 'index.html', data)


# Signup codes
class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        firstname = postData.get('firstname')
        lastname = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        reEnterpassword = postData.get('ReEnterpassword')
        error_message = None
        customer = Customer(firstname=firstname,
                            lastname=lastname,
                            phone=phone,
                            email=email,
                            password=password)
        if (not firstname):
            error_message = "Firsr Name is required!"
        elif len(firstname) < 4:
            error_message = "First Name must be 4 char long or more!"
        elif (not lastname):
            error_message = 'Last Name is required!'
        elif len(lastname) < 4:
            error_message = "Last Name must be 4 char long or more"
        elif (not phone):
            error_message = 'Phone Number is required!'
        elif (not email):
            error_message = 'Email is required!'

        elif (not password):
            error_message = 'Password is required!'
        elif (not reEnterpassword) == password:
            error_message = 'Re Enter the password!'
        elif customer.isExists():
            error_message = 'Email address already Exists !'
        value = {
            'firstname': firstname,
            'lastname': lastname,
            'phone': phone,
            'email': email,
            'password': password
        }

        if not error_message:
            customer.password = make_password(customer.password)

            customer.register()
            return redirect('homepage')
        else:

            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)


# Login code
class Login(View):
    return_url=None
    def get(self, request):
        Login.return_url=request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                # request.session['customer_id'] = customer.id
                request.session['customer'] = customer.id
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url=None
                    return redirect('homepage')
                # request.session['email'] = customer.email

            else:
                error_message = "invalid email or password!!"

        else:
            error_message = 'Email or password invalid!!'

        return render(request, 'login.html', {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect('login')


def Cart(request):
    ids = list(request.session.get('cart').keys())
    products = Product.get_product_by_id(ids)
    print(products)
    return render(request, 'cart.html', {'products': products})


class Checkout(View):
    def post(self, request):
        name = request.POST.get("name")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        customer = request.session.get("customer")
        cart = request.session.get("cart")
        products = Product.get_product_by_id(list(cart.keys()))
        # print(name, address,phone,customer,cart,products)
        print(address, phone, customer, cart, products)
        for product in products:
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}
        return redirect('cart')


class OrderView(View):
    @method_decorator(auth_middleware)
    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request, 'orders.html', {'orders': orders})


def contact(request):
    if request.method == 'POST':
        contact = Contact(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')

        )
        contact.save()
        message = 'Your email has been sent THANKS!'

    return render(request, 'contact.html')

def payments(request):

    return render(request,'payments.html')
