from tkinter import image_types
from django.contrib import admin
from .models import Product
from .models import Category
from .models import Customer
from .models import Order, Contact


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'description', 'picture']


admin.site.register(Product, ProductAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'phone', 'email', 'password']


admin.site.register(Customer, CustomerAdmin)

admin.site.register(Order)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['email','name']


admin.site.register(Contact, ContactAdmin)
