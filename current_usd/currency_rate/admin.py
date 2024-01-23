from django.contrib import admin

from .models import CurrencyRate


class CurrencyRateAdmin(admin.ModelAdmin):
    list_display = ('currency', 'rate', 'date')
    list_filter = ('currency', 'date')


admin.site.register(CurrencyRate, CurrencyRateAdmin)
