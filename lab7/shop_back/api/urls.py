from django.urls import path
from . import views


urlpatterns = [
    path('products/', view=views.ProductView.as_view({'get': 'list'}))
]
