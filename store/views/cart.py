from django import views
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from .import Product
from .import Category
from .import Customer
# Cart code
# class Cart(View):
#     def get(self, request):
#         return render(request, 'cart.html')
