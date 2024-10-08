from django.db import models

from users.constants import (MAX_LENGTH_ABOUT_TEAM, MAX_LENGTH_FIRSTNAME,
                             MAX_LENGTH_ICON,
                             MAX_LENGTH_KEY_EMPLOYEE,
                             MAX_LENGTH_LASTNAME,
                             MAX_LENGTH_ROLE,
                             MAX_LENGTH_URL_CONFLUENCE,
                             MAX_LENGTH_URL_JIRA)
from skills.models import Grade


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
    """Модель Team (Команда)."""

    about_team = models.CharField(verbose_name='Краткая информация о команде',
                                  max_length=MAX_LENGTH_ABOUT_TEAM)
    url_confluence = models.CharField(
        verbose_name='Ссылка на пространство команды в конфлюенс',
        max_length=MAX_LENGTH_URL_CONFLUENCE)
    url_jira = models.CharField(verbose_name='Ссылка на jira команды',
                                max_length=MAX_LENGTH_URL_JIRA)
    team_lead = models.ForeignKey(Employee,
                                  verbose_name='id тимлида',
                                  related_name='teams') 
    product_owner = models.ForeignKey(Employee,
                                      verbose_name='id продукт оунера',
                                      related_name='teams',
                                      on_delete=models.CASCADE)


class User_s_teams(models.Model):
    """Модель User's teams (Данные о правах пользователей)."""

    id_team = 
    rights = 


class Team_s_employees(models.Model):
    """Модель Team's employees (Данные о сотрудниках в командах)."""

    id_team = 
    rights =
