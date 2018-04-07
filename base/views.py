from django.shortcuts import render
from product.models import Product, Product_image

def base(request):
    
    session_key = request.session.session_key

    print('session key: ', request.session.session_key)
    products_items = Product_image.objects.filter(is_main=True, is_active=True, product__is_active=True)
    products_items_phones = products_items.filter(is_main=True, is_active=True, product__category_id=1)
    products_items_laptops = products_items.filter(is_main=True, is_active=True, product__category_id=2)
    return render(request, 'base/home.html', locals())
