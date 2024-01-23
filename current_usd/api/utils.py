from http import HTTPStatus

import requests
from constants import CURRENCY, TIMEOUT, URL
from exceptions import StatusCodeNotOk
from django.conf import settings


def get_api_answer():
    """
    Делает запрос к внешнему API для получения курса доллара.
    """
    endpoint = f'{URL}?apikey={settings.API_KEY}&currencies={CURRENCY}'
    try:
        response = requests.get(endpoint, timeout=TIMEOUT)
        if response.status_code == HTTPStatus.OK:
            return response.json()
        else:
            raise StatusCodeNotOk(response.status_code)
    except Exception as error:
        raise ConnectionError('Ошибка при запросе к API') from error
