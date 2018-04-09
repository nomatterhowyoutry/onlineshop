from django.conf import settings
from .models import Currency

def currency(request):
    currencies = Currency.objects.all()
    DISPLAY_CURRENCY = settings.DISPLAY_CURRENCY
    return locals()