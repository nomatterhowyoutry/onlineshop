from django.contrib import admin
from .models import *

class Product_imageInline(admin.TabularInline):
    model = Product_image
    extra = 0

class Product_priceInline(admin.StackedInline):
    model = Product_price
    fk_value = 'price' 

class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    # list_display.append('get_productprice_value')
    list_select_related = True
    inlines = [Product_priceInline, Product_imageInline]

    list_display.append('price')

    # def get_productprice_value(self, instance):
    #     return instance.price

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Currency._meta.fields]

    class Meta:
        model = Currency

admin.site.register(Currency, CurrencyAdmin)

class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ExchangeRate._meta.fields]

    class Meta:
        model = ExchangeRate

admin.site.register(ExchangeRate, ExchangeRateAdmin)

class Product_priceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product_price._meta.fields]

    class Meta:
        model = Product

admin.site.register(Product_price, Product_priceAdmin)


class Product_imageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product_image._meta.fields]

    class Meta:
        model = Product_image

admin.site.register(Product_image, Product_imageAdmin)

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]

    class Meta:
        model = ProductCategory

admin.site.register(ProductCategory, ProductCategoryAdmin)
