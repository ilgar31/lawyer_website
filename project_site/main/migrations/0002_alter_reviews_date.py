# Generated by Django 4.2.6 on 2024-02-06 20:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 6, 20, 17, 9, 78542, tzinfo=datetime.timezone.utc), verbose_name='Дата и время отзыва'),
        ),
    ]