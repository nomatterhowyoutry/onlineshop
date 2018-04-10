from django.urls import path
from . import views

urlpatterns = [
    path('cart_adding/', views.cart_adding, name='cart_adding'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/cart_adding/', views.cart_adding, name='cart_adding'),
]