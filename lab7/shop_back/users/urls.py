from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path


router = DefaultRouter()

router.register('users', views.UserViewSet, basename='users')
urlpatterns = [
    path('users/register/', views.UserViewSet.as_view({'post': 'create'}), name='user-register'),
]

urlpatterns += router.urls