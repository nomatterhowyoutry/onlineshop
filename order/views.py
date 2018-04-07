from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .forms import Checkout_form
from django.contrib.auth.models import User

def cart_adding(request):
    return_dict = dict()

    session_key = request.session.session_key

    print(request.POST)

    data = request.POST
    product_id = data.get('product_id')
    quantity = data.get('quantity')
    is_delete = data.get('is_delete')

    if is_delete == 'true':
        print('Deleting from cart: product_id:{}, quantity:{}'.format(product_id, quantity))
        Product_in_cart.objects.filter(id=product_id).update(is_active=False)
    else:
        new_product, created = Product_in_cart.objects.get_or_create(
            session_key=session_key, product_id=product_id, is_active=True, defaults={'quantity':quantity})
        if not created:
            new_product.quantity += int(quantity)
            new_product.save(force_update=True)

    products_total_quantity = Product_in_cart.objects.filter(
        session_key=session_key, is_active=True).count()

    products_in_cart = Product_in_cart.objects.filter(session_key=session_key, is_active=True)
    products_total_quantity = products_in_cart.count()

    return_dict['products_total_quantity'] = products_total_quantity
    return_dict['products'] = list()

    for item in products_in_cart:
        product_dict = dict()
        product_dict['id'] = item.id
        product_dict['name'] = item.product.name
        product_dict['quantity'] = item.quantity
        product_dict['price_per_item'] = item.product.price
        product_dict['total_price'] = item.total_price
        return_dict['products'].append(product_dict)

    return JsonResponse(return_dict)

def checkout(request):

    session_key = request.session.session_key

    print('session key: ', request.session.session_key)

    products_in_cart = Product_in_cart.objects.filter(session_key=session_key, is_active=True)

    form = Checkout_form(request.POST or None)

    if request.POST:
        print(request.POST)
        if form.is_valid():
            print('form is valid')
            data = request.POST
            phone = data['phone']
            name = data['name']
            user, created = User.objects.get_or_create(username=phone, defaults={'first_name':name})

            order = Order.objects.create(user=user, customer_name=name, customer_phone=phone, status_id=1)

            for key, value in data.items():
                if key.startswith('product_in_cart_'):
                    product_in_cart_id = key.split('product_in_cart_')[1]
                    product_in_cart = Product_in_cart.objects.get(id=product_in_cart_id)
                    product_in_cart.quantity = int(value)
                    product_in_cart.order = order
                    product_in_cart.save(force_update=True)

                    Product_in_order.objects.create(
                        order = order,
                        product=product_in_cart.product, 
                        quantity=product_in_cart.quantity, 
                        price_per_item=product_in_cart.price_per_item, 
                        total_price=product_in_cart.total_price)

                    product_in_cart.is_active = False
                    product_in_cart.save()
        else:
            print('form is not valid')

    return render(request, 'order/checkout.html', locals())




