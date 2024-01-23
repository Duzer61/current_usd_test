from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CurrentUsdViewSet

app_name = 'api'

router = DefaultRouter()
router.register('get-current-usd', CurrentUsdViewSet, 'get-current-usd')

urlpatterns = [
    path('', include(router.urls)),
]
