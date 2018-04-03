from django.shortcuts import render
from product.models import *


def product(request, product_id):
    product = Product.objects.get(id=product_id)

    session_key = request.session.session_key

    if not session_key:
        request.session.cycle_key()

    print('session key: ', request.session.session_key)

    return render(request, 'product/product.html', locals())