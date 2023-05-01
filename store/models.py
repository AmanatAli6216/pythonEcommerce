from distutils.command.upload import upload
import email
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import EmailField
import datetime


# Create your models here.

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Product Model
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, default=1)
    description = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in=ids)

    #
    @staticmethod
    def get_all_prodect_by_category_id(catetory_id):
        if catetory_id:
            return Product.objects.filter(category=catetory_id)
        else:
            return Product.objects.all

    def get_all_prodect(catetory_id):
        return Product.objects.all

    # Customer Model


class Customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
        self.save()

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True

        return False

    @staticmethod
    def get_customer_by_email(email):
        try:

            return Customer.objects.get(email=email)
        except:
            return False


# OrderModel

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=300)
    def __str__(self):
        return self.email
