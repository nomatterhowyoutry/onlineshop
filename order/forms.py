from django import forms
from phonenumber_field.formfields import PhoneNumberField

class Checkout_form(forms.Form):
    name = forms.CharField(required=True)
    phone = PhoneNumberField(required=True)
