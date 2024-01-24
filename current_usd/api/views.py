from rest_framework import viewsets
from currency_rate.models import CurrencyRate
from constants import CACHE_TIME, CURRENCY, PAST_RATES_NUM
from .serializers import RatesSerializer
from .utils import get_actual_rate
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class CurrentUsdViewSet(viewsets.ViewSet):
    """
    Вьюсет для запроса текущего курса доллара и отображение
    вместе с предыдущими курсами.
    """
    @method_decorator(cache_page(CACHE_TIME))
    def list(self, request):
        print("-------------Делаем запрос курса доллара----------------------")
        past_data = (
            CurrencyRate.objects.filter(currency=CURRENCY)[:PAST_RATES_NUM]
        )
        serialized_past_data = RatesSerializer(past_data, many=True).data
        rate = get_actual_rate()
        if isinstance(rate, float):
            print('Получен текущий курс доллара:', rate)
            CurrencyRate.objects.create(currency=CURRENCY, rate=rate)
            current_result = rate
        else:
            current_result = {'error': rate}
        print("Сейчас вернем результат")
        return Response({
            'currency': CURRENCY,
            'current_rate': current_result,
            'past_rates': serialized_past_data
        })
