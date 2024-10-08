from django.conf import settings
from django.db import models

from skills.constants import (MAX_LENGTH_KEY_SKILL, MAX_LENGTH_REQUIRED_LEVEL)
from users.models import Team, Team_s_employees


class Grade(models.Model):
    """Модель грейда сотрудника"""

    name_grade = models.TextField(
        choices=settings.GRADE,
        verbose_name='Грейд',
    )


class Skill(models.Model):
    """Модель Skill (Данные о навыках)"""

    pass


class Team_s_skills(models.Model):
    """Модель Team's skills (Данные о навыках команды)."""

    id_team = models.ForeignKey(Team,
                                verbose_name='Идентификатор команды',
                                related_name='team_s_skills',
                                on_delete=models.CASCADE)
    id_skill = models.ForeignKey(Skill,
                                 verbose_name='Идентификатор навыка',
                                 related_name='team_s_skills',
                                 on_delete=models.CASCADE)
    key_skill = models.BooleanField(
        verbose_name='Флаг, является ли навык ключевым',
        max_length=MAX_LENGTH_KEY_SKILL)
    required_level = models.CharField(
        verbose_name='Необходимый уровень владения навыком',
        max_length=MAX_LENGTH_REQUIRED_LEVEL)
    required_count_employees = models.PositiveIntegerField(
        verbose_name=('Количество сотрудников в команде,'
                      'которые должны обладать навыком'),
        max_length=max(Team_s_employees.id))
