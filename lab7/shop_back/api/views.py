from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework import status, permissions
from rest_framework.viewsets import ModelViewSet
from api import models, serializers
from order.serializers import OrderSerializer


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

    @action(detail=True, methods=['post'], url_path='buy')
    def buy_product(self, request, pk=None):
        product = self.get_object()

        if not request.user.is_authenticated:
            return Response({"message": "Authentication is required to buy this product"}, status=status.HTTP_401_UNAUTHORIZED)
        order_data = {'product_id': product.id, 'user_id': request.user.id}
        serializer = OrderSerializer(data=order_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Order created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
