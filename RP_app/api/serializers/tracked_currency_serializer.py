from rest_framework import serializers
from RP_app.api.models import TrackedCurrency
from RP_app.api.services.tracked_currency_service import TrackedCurrencyService

"""
Сериалайзер для обработки POST запроса на добавление облеживаемых объектов.
"""


class AddTrackedSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackedCurrency
        fields = ["currency", "threshold"]

    def create(self, validated_data):
        currency = validated_data['currency']
        threshold = validated_data['threshold']
        email = validated_data['email']
        result = TrackedCurrencyService().add_tracked_currency(email=email, currency_id=currency,
                                                               threshold=float(threshold))
        return result


class UpdateTrackedSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackedCurrency
        fields = ["threshold"]


class DeleteTrackedSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackedCurrency
        fields = ["currency", "threshold"]

    def create(self, validated_data):
        currency = validated_data['currency']
        email = validated_data['email']
        result = TrackedCurrencyService().delete_tracked_currency(email=email, currency_id=currency)
        return result
