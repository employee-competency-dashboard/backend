from django.conf import settings
from django.db import models


class Grade(models.Model):
    'Модель грейда сотрудника'

    grade = models.TextField(
        choices=settings.GRADE,
        verbose_name='Грэйд',
    )
