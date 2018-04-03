from .models import Product_in_cart

def getting_cart_info(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    products_in_cart = Product_in_cart.objects.filter(session_key=session_key, is_active=True)
    products_total_quantity = products_in_cart.count()

    return locals()