from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('product_api', views.Product_View)

urlpatterns = [
    path('product/<product_id>/', views.product, name='product'),
    path('', include(router.urls)),
]