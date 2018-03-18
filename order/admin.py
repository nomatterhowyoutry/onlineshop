from django.contrib import admin
from .models import *

class Product_in_orderInline(admin.TabularInline):
    model = Product_in_order
    extra = 0

class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [Product_in_orderInline]

    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)

class Product_in_orderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product_in_order._meta.fields]

    class Meta:
        model = Product_in_order

admin.site.register(Product_in_order, Product_in_orderAdmin)
