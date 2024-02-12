from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework import status, permissions
from rest_framework.viewsets import ModelViewSet
from api import models, serializers


@api_view()
def index(request):
    products = models.Product.objects.filter(
        is_active=True, quantity__gt=0
    ).first()
    serializer = serializers.ProductSerializer(products)

    return Response(serializer.data)


class ProductView(ModelViewSet):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.select_related('category')
    permission_classes = (permissions.AllowAny,)

@api_view()
def buy(request, *args, **kwargs):
    if request.method == "GET":
        print(request.user)
        return Response(data={'message': 'ok'})


class CategoryView(ModelViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()
    permission_classes = (permissions.AllowAny,)

    @action(detail=True, methods=['get'], url_path='products')
    def list_products(self, request, pk=None):
        category = self.get_object()
        products = category.product.filter(is_active=True)
        serializer = serializers.ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
