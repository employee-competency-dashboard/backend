from django.conf import settings
from django.db import models

from users_skills.constants import (DOMEN,
                                    GRADE,
                                    EXPERTISE,
                                    MAX_LENGTH_ABOUT_TEAM,
                                    MAX_LENGTH_FIRSTNAME,
                                    MAX_LENGTH_KEY_EMPLOYEE,
                                    MAX_LENGTH_KEY_SKILL,
                                    MAX_LENGTH_LASTNAME,
                                    MAX_LENGTH_REQUIRED_LEVEL,
                                    MAX_LENGTH_RIGHTS,
                                    MAX_LENGTH_ROLE,
                                    MAX_LENGTH_URL_CONFLUENCE,
                                    MAX_LENGTH_URL_JIRA,
                                    RIGHT,
                                    SKILL)


class Grade(models.Model):
    """Модель грейда сотрудника"""

    name_grade = models.CharField(
        choices=GRADE,
        verbose_name='Грейд',
    )


class Expertise(models.Model):
    """Модель компетенции сотрудника

    В отдельную модель не выносим ?    
    """

    pass


class Skill(models.Model):
    """Модель Skill (Данные о навыках)"""

    skill_name = models.CharField(
        choices=SKILL,
        verbose_name='Навык',
    )
    skill_type = models.CharField(
        choices=DOMEN,
        verbose_name='Хард или Софт',

    )
    name_expertise=models.CharField(
        choices=EXPERTISE,
        verbose_name='Компетенция'
    )
    


class Employee(models.Model):
    """Модель Employee (Данные о сотрудниках)."""

    firstName = models.CharField(verbose_name='Имя сотрудника',
                                 max_length=MAX_LENGTH_FIRSTNAME)
    lastName = models.CharField(verbose_name='Фамилия сотрудника',
                                max_length=MAX_LENGTH_LASTNAME)
    role = models.CharField(
        verbose_name='Роль сотрудника в команде (должность)',
        max_length=MAX_LENGTH_ROLE)
    id_grade = models.ForeignKey(
        Grade,
        verbose_name='Идентификатор грейда сотрудника',
        related_name='employees',
        on_delete=models.CASCADE)    
    key_employee = models.BooleanField(
        verbose_name='Является ли сотрудник ключевым',
        max_length=MAX_LENGTH_KEY_EMPLOYEE)
    icon = models.ImageField(verbose_name='Ссылка на иконку сотрудника',
                             upload_to='users/images/',
                             null=True)


class Team(models.Model):
    """Модель Team (Данные о команде)."""

    about_team = models.CharField(verbose_name='Краткая информация о команде',
                                  max_length=MAX_LENGTH_ABOUT_TEAM)
    url_confluence = models.CharField(
        verbose_name='Ссылка на пространство команды в конфлюенс',
        max_length=MAX_LENGTH_URL_CONFLUENCE)
    url_jira = models.CharField(verbose_name='Ссылка на jira команды',
                                max_length=MAX_LENGTH_URL_JIRA)
    team_lead = models.ForeignKey(Employee,
                                  verbose_name='id тимлида',
                                  related_name='teams',
                                  on_delete=models.SET_NULL)
    product_owner = models.ForeignKey(Employee,
                                      verbose_name='id продукт оунера',
                                      related_name='teams',
                                      on_delete=models.CASCADE)


class User_s_teams(models.Model):
    """Модель User's teams (Данные о правах пользователей)."""

    id_employee = models.ForeignKey(Employee,
                                    verbose_name='Идентификатор сотрудника',
                                    related_name='user_s_teams',
                                    on_delete=models.CASCADE)
    id_team = models.ForeignKey(Team,
                                verbose_name='Идентификатор команды',
                                related_name='user_s_teams',
                                on_delete=models.CASCADE)
    rights = models.CharField(
        verbose_name='Права сотрудника для работы с дашбордом команды',
        choices=settings.RIGHT,
        max_length=MAX_LENGTH_RIGHTS)


class Team_s_employees(models.Model):
    """Модель Team's employees (Данные о сотрудниках в командах)."""

    id_employee = models.ForeignKey(Employee,
                                    verbose_name='Идентификатор сотрудника',
                                    related_name='team_s_employees',
                                    on_delete=models.CASCADE)
    id_team = models.ForeignKey(Team,
                                verbose_name='Идентификатор команды',
                                related_name='team_s_employees',
                                on_delete=models.CASCADE)


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
        max_length=64)
