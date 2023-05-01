from django import views
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from .import Product
from .import Category
from .import Customer





#Login code
class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.get_customer_by_email(email)
        error_message=None
        if customer:
            flag=check_password(password, customer.password)
            if flag:
                return redirect('homepage')
            else:
                error_message="invalid email or password!!"

        else:
            error_message='Email or password invalid!!'

        return render(request, 'login.html', {'error': error_message})    

def logout(request):
    request.session.clear()
    return redirect('login')