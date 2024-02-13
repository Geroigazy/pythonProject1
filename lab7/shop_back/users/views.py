from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import status, permissions
from . import serializers, exceptions
from order.models import Order
from order.serializers import OrderSerializer
from django.contrib.auth import get_user_model


User = get_user_model()

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'create_token':
            return serializers.CreateUserToken
        elif self.action == 'create':
            return serializers.UserRegistrationSerializer
        
        return serializers.UserSerializer

    @action(detail=False, url_path='login', methods=('POST',))
    def create_token(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        users = User.objects.filter(username=serializer.validated_data['username'])

        if not users.exists():
            raise exceptions.UserNotFounded

        user = users.first()

        if not user.check_password(serializer.validated_data['password']):
            raise exceptions.InvalidCrededntials

        access = AccessToken.for_user(user)

        return Response({
            'access': str(access)
        }, status=status.HTTP_201_CREATED)   


    @action(detail=True, url_path='orders', methods=('GET',))
    def get_orders(self, request, pk=None):
        user = self.get_object()
        orders = Order.objects.filter(user_id=user.id)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
