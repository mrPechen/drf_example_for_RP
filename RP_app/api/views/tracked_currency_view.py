from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from RP_app.api.models import TrackedCurrency
from RP_app.api.serializers.tracked_currency_serializer import AddTrackedSerializer, UpdateTrackedSerializer
from django.shortcuts import get_object_or_404

"""
Обработка запроса на добавление отслеживаемых объектов.
"""


@swagger_auto_schema(method='POST', request_body=AddTrackedSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_tracked_currency(request):
    if request.method == 'POST':
        serializer = AddTrackedSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = request.user.email
        serializer.save(email=email)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@swagger_auto_schema(method='PATCH', request_body=UpdateTrackedSerializer)
@api_view(['DELETE', 'PATCH'])
@permission_classes([IsAuthenticated])
def patch_or_delete_tracked_currency(request, id: int):
    email = request.user.email
    result = get_object_or_404(TrackedCurrency, user__email=email, currency=id)

    if request.method == 'DELETE':
        result.delete()
        return Response(data={"success": f"currency_id: {id} was deleted from your tracked list."},
                        status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PATCH':
        serializer = UpdateTrackedSerializer(result, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={"success": f"Your threshold for currency_id: {id} was updated to {request.data['threshold']}."},
                status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
