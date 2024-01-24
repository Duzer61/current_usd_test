from http import HTTPStatus

import requests
from constants import CURRENCY, TIMEOUT, URL
from .exceptions import StatusCodeNotOk
from django.conf import settings


def get_api_answer(currency):
    """
    Делает запрос к внешнему API для получения курса доллара.
    """
    endpoint = f'{URL}?apikey={settings.API_KEY}&currencies={currency}'
    try:
        response = requests.get(endpoint, timeout=TIMEOUT)
        if response.status_code == HTTPStatus.OK:
            return response.json()
        else:
            raise StatusCodeNotOk(response.status_code)
    except Exception as error:
        raise ConnectionError(f'Ошибка при запросе к API: {error}')


def check_response(response, currency):
    """
    Проверяет ответ API на корректность.
    """

    if not isinstance(response, dict):
        raise TypeError(
            f'Структура данных API не соответствует ожиданию. '
            f'Получен {type(response)} вместо <dict>'
        )

    if 'data' not in response:
        raise KeyError('В ответе API нет ключа <data>')

    if not isinstance(response['data'], dict):
        raise TypeError(
            f'Структура данных API не соответствует ожиданию. '
            f'Получен {type(response["data"])} вместо <dict>'
        )

    if currency not in response['data']:
        raise KeyError(f'В ответе API нет ключа <{currency}>')

    if not isinstance(response['data'][currency], float):
        raise TypeError(
            f'Структура данных API не соответствует ожиданию. '
            f'Получен {type(response["data"][currency])} вместо <float>'
        )
    rate = response['data'][currency]
    return rate


def get_actual_rate():
    """
    Возвращает актуальный курс доллара к выбранной валюте.
    """

    try:
        response = get_api_answer(CURRENCY)
        rate = check_response(response, CURRENCY)
    except Exception as error:
        print(error)
        print('А теперь в строку')
        print(str(error))
        return str(error)
    return rate
