from django.conf import settings
from django.db import models


class Skill(models.Model):
    'Модель навыка сотрудника'

    skill_name = models.CharField(
        choices=settings.SKILL,
        verbose_name='Название навыка',
    )
    skill_type = models.CharField(
        choices=settings.TYPE,
        verbose_name='Тип навыка',
    )
    id_expertise  = models.ManyToManyField(

    )







class Grade(models.Model):
    'Модель грейда сотрудника'

    grade = models.CharField(
        choices=settings.GRADE,
        verbose_name='Грэйд',
    )
