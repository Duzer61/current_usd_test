from django.shortcuts import render
from rest_framework import viewsets


class CurrentUsdViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Вьюсет для запроса текущего курса доллара.
    """
    pass