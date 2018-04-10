from django.contrib import admin
from .models import *

class Product_imageInline(admin.TabularInline):
    model = Product_image
    extra = 0

class Product_priceInline(admin.StackedInline):
    model = Product_price
    fk_value = 'price' 

class ProductSubcategoryInline(admin.StackedInline):
    model = ProductSubcategory
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    list_select_related = True
    inlines = [Product_priceInline, Product_imageInline]

    list_display.append('price')

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Currency._meta.fields]

    class Meta:
        model = Currency

admin.site.register(Currency, CurrencyAdmin)

class ProductSubcategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductSubcategory._meta.fields]

    class Meta:
        model = ProductSubcategory

admin.site.register(ProductSubcategory, ProductSubcategoryAdmin)

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
    inlines = [ProductSubcategoryInline]

    class Meta:
        model = ProductCategory

admin.site.register(ProductCategory, ProductCategoryAdmin)
