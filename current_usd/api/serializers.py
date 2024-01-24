from rest_framework import serializers
from currency_rate.models import CurrencyRate


class RatesSerializer(serializers.ModelSerializer):
    """
    Сериализатор для курсов валюты.
    """

    class Meta:
        model = CurrencyRate
        fields = ['rate', 'date']
