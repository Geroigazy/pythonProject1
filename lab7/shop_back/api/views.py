from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ViewSet
from api import models, serializers

@api_view()
def index(request):
    products = models.Product.objects.filter(
        is_active = True, quantity__gt = 0
    ).first()
    serializer = serializers.ProductSerializer(products)

    return Response(serializer.data)

# http://127.0.0.1:8000/api/products/
class ProductView(ViewSet):

    def list(self, request):
        query_set = models.Product.objects.filter(
            is_active = True, quantity__gt = 0
        )
        serializer = serializers.ProductSerializer(query_set, many=True)
        return Response(serializer.data)
