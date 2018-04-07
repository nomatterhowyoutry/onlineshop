from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import Product_Serializer
from .models import *


def product(request, product_id):
    product = Product.objects.get(id=product_id)

    session_key = request.session.session_key

    if not request.session.exists(request.session.session_key):
        session_key = request.session.create() 

    print('session key: ', request.session.session_key)

    return render(request, 'product/product.html', locals())


class Product_View(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Product_Serializer