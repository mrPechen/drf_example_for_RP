from rest_framework import serializers
from RP_app.api.models import User

from RP_app.api.services.user_service import UserService

"""
Сериалайзер для обработки POST запроса на регистрацию пользователя.
"""


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password"]

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        user = UserService().create_user(email=email, password=password)
        return user
