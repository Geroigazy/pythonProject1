from rest_framework import serializers



class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    price = serializers.FloatField()
    description = serializers.CharField()
    quantity = serializers.IntegerField()
    category_id = serializers.RelatedField(source='category', read_only=True)
    is_active = serializers.BooleanField()