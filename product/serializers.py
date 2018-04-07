from .models import *
from rest_framework import serializers

#HyperlinkedModelSerializer

class Product_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id', 'url', 'name', 'price', 'discount', 'category',
            'description', 'short_description', 'is_active')