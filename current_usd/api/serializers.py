from currency_rate.models import CurrencyRate
from rest_framework import serializers


class RatesSerializer(serializers.ModelSerializer):
    """
    Сериализатор для курсов валюты.
    """

    class Meta:
        model = CurrencyRate
        fields = ['rate', 'date']
