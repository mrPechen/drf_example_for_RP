from typing import Any

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from RP_app.api.serializers.user_serializers import UserSerializer

"""
Обработка запроса на создание нового пользователя.
"""


@swagger_auto_schema(method='POST', request_body=UserSerializer)
@api_view(['POST'])
def registration_new_user(request: Any):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)
