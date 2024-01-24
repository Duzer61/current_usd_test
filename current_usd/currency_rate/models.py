from django.db import models


class CurrencyRate(models.Model):
    """
    Модель курса валют.
    """

    currency = models.CharField(verbose_name='Код валюты', max_length=3)
    rate = models.FloatField(verbose_name='Курс')
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True)

    class Meta:
        verbose_name = 'Курс валюты'
        verbose_name_plural = 'Курсы валют'
        ordering = ['-date']

    def __str__(self):
        return f'{self.currency}: {self.rate}'
