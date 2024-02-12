from . import serializers, models
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, status


class OrderViewSet(ModelViewSet):
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        return models.Order.objects.filter(user_id=self.request.user)

