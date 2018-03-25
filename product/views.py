from django.shortcuts import render
from product.models import *


def product(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product/product.html', locals())