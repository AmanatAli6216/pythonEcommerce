from django.urls import path
from .views import views
from .views import Signup, Index
from .views import Login
from .views import Login
from .views import logout
# from .views import cart
from .views import Cart
from .views import Checkout
from .views import OrderView
from .views import payments
from .views import contact

from .auth import auth_middleware
urlpatterns = [
    path('', Index.as_view(), name="homepage"),
    path('signup', Signup.as_view()),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', auth_middleware(Cart), name='cart'),
    path('check-out', Checkout.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('payments', payments, name='payments'),
    path('contact',contact, name='contact'),

]
