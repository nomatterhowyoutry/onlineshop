from django.conf import settings

def currency(request):
    return {'DISPLAY_CURRENCY': settings.DISPLAY_CURRENCY}