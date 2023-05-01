from django import views
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from .import Product
from .import Category
from .import Customer


# Create your views here.
def index(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    product=None
    category=Category.objects.all
    categoryID=request.GET.get('category')
    if categoryID:
        product=Product.get_all_prodect_by_category_id(categoryID)
    else:
        product=Product.objects.all
    data={}
    data['product']=product
    data['category']=category
    #customerinfo=request.session.get('email')
    return render(request,'index.html',data)#,customerinfo)
