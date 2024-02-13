from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('order', views.OrderViewSet, basename='order')

urlpatterns = router.urls
