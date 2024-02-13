from rest_framework import serializers
from . import models
from api.serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = '__all__'

class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Order
        fields = ['product_id']
