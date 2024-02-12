from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', views.ProductView, basename='products')
router.register('categories', views.CategoryView, basename='categories')

urlpatterns = router.urls
