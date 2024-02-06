from django.db import models
from datetime import datetime
from django.utils import timezone



class Reviews(models.Model):
    name = models.CharField("ФИО", max_length=45, blank=True)
    review = models.CharField("Отзыв", max_length=45, blank=True)
    date = models.DateTimeField("Дата и время отзыва", default=datetime.now(tz=timezone.utc), blank=True)


    def __str__(self):
        return f'{self.name} {self.date}'

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"