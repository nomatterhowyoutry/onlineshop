from django.urls import path
from base import views

urlpatterns = [
    path('', views.base, name='base'),
    path('change_currency/', views.change_currency, name='change_currency'),
]