from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class CreateUserToken(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'credit_card']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user