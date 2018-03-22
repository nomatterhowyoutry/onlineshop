from django.shortcuts import render
from product.models import Product, Product_image
# from django.http import HttpResponse

def base(request):
    # products = Product.objects.filter(is_active=True)
    products_images = Product_image.objects.filter(is_main=True, is_active=True)
    return render(request, 'base/home.html', locals())
