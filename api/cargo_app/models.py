from django.db import models


class Status(models.Model):
    name_status = models.CharField(max_length=200, unique=True, db_index=True)

    def __str__(self):
        return f'{self.name_status} {self.pk}'

    class Meta:
        verbose_name = 'Статус Заказа'
        verbose_name_plural = 'Статусы Заказов'


class TrackCode(models.Model):
    code = models.CharField(max_length=300, unique=True, default='', verbose_name='Код для отслеживания статуса заказа',
                            db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default='', verbose_name='статус')
    date = models.DateTimeField(verbose_name='Время', )

    def __str__(self):
        return f'Трек код :{self.code[:5]} Дата создание и время создания кода {self.created}'

    class Meta:
        verbose_name = 'Трек Код'
        verbose_name_plural = 'Трек Коды'
