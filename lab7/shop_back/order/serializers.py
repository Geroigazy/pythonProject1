from rest_framework import serializers
from . import models
from api.serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = '__all__'
