import random
from django.db import models

from users_skills.constants import (MAX_LENGTH_ABOUT_TEAM,
                                    MAX_LENGTH_FIRST_NAME,
                                    MAX_LENGTH_GRADE,
                                    MAX_LENGTH_KEY_SKILL,
                                    MAX_LENGTH_LAST_NAME,
                                    MAX_LENGTH_LEVEL,
                                    MAX_LENGTH_NAME_EXPERTISE,
                                    MAX_LENGTH_REQUIRED_LEVEL,
                                    MAX_LENGTH_REQ_LEVEL_GRADE,
                                    MAX_LENGTH_RIGHTS,
                                    MAX_LENGTH_ROLE,
                                    MAX_LENGTH_STATUS,
                                    MAX_LENGTH_URL_CONFLUENCE,
                                    MAX_LENGTH_URL_JIRA, EXPERTISE,
                                    RIGHT, GRADE, STATUS, LEVEL)


class Expertise(models.Model):
    """Модель Expertise (Данные о компетенциях)."""

    REQUIRED_FIELDS = ['name_expertise']

    name_expertise = models.CharField(
        verbose_name='Название компетенции',
        choices=EXPERTISE,
        max_length=MAX_LENGTH_NAME_EXPERTISE)

    class Meta:
        verbose_name = 'Компетенция'
        verbose_name_plural = 'Компетенции'
        ordering = ('name_expertise',)

    def __str__(self):
        return self.name_expertise


class Skill(models.Model):
    """Модель Skill (Навыки)."""

    LEVEL_CHOICES = [
        ('none', 'None'),
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]

    STATUS_CHOICES = [
        ('low', 'Low'),
        ('normal', 'Normal'),
        ('improving', 'Improving'),
    ]

    skill = models.CharField(verbose_name='Навык',
                             max_length=100)
    level = models.CharField(verbose_name='Уровень',
                             choices=LEVEL_CHOICES, max_length=50)    
    status = models.CharField(verbose_name='Статус',
                              choices=STATUS_CHOICES, max_length=50)

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.skill


class Employee(models.Model):
    """Модель Employee (Данные о сотрудниках)."""

    REQUIRED_FIELDS = ['first_name', 'last_name', 'role',
                       'grade', 'key_employee', 'userPhoto']

    userPhoto = models.ImageField(verbose_name='Ссылка на иконку сотрудника',
                             upload_to='users/images/',
                             null=True)
    first_name = models.CharField(verbose_name='Имя сотрудника',
                                  max_length=MAX_LENGTH_FIRST_NAME)
    last_name = models.CharField(verbose_name='Фамилия сотрудника',
                                 max_length=MAX_LENGTH_LAST_NAME)
    key_employee = models.BooleanField(verbose_name='Является ли сотрудник ключевым',
                                       default=False)
    role = models.CharField(verbose_name='Роль сотрудника в команде (должность)',
                            max_length=MAX_LENGTH_ROLE)
    grade = models.CharField(verbose_name='Идентификатор грейда сотрудника',
                             choices=GRADE,
                             max_length=MAX_LENGTH_GRADE)
    skills = models.ManyToManyField(Skill, verbose_name='Навыки сотрудников',
                                    related_name='employees')
    expertise = models.FloatField(verbose_name='Экспертность', default=0.0)
    progress = models.FloatField(verbose_name='Прогресс', default=0.0)

    def save(self, *args, **kwargs):
        self.expertise = random.uniform(0.5, 0.95)
        self.progress = random.uniform(0.5, 0.95)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ('last_name',)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Team(models.Model):
    """Модель Team (Данные о команде)."""

    REQUIRED_FIELDS = ['about_team', 'url_confluence', 'url_jira',
                       'team_lead', 'product_owner']

    about_team = models.CharField(verbose_name='Краткая информация о команде',
                                  max_length=MAX_LENGTH_ABOUT_TEAM)
    url_confluence = models.CharField(
        verbose_name='Ссылка на пространство команды в конфлюенс',
        max_length=MAX_LENGTH_URL_CONFLUENCE)
    url_jira = models.CharField(verbose_name='Ссылка на jira команды',
                                max_length=MAX_LENGTH_URL_JIRA)
    team_lead = models.ForeignKey(Employee,
                                  verbose_name='id тимлида',
                                  related_name='teams_team_lead',
                                  null=True,
                                  on_delete=models.SET_NULL)
    product_owner = models.ForeignKey(Employee,
                                      verbose_name='id продукт оунера',
                                      related_name='teams_product_owner',
                                      null=True,
                                      on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'
        ordering = ('id',)

    def __str__(self):
        return f'Номер команды: {self.id}'


class User_s_teams(models.Model):
    "Модель User's teams (Данные о правах пользователей)."


    last_name = models.ForeignKey(Employee,
                                    verbose_name='Идентификатор сотрудника',
                                    related_name='user_s_teams',
                                    on_delete=models.CASCADE)
    id_team = models.ForeignKey(Team,
                                verbose_name='Идентификатор команды',
                                related_name='user_s_teams',
                                on_delete=models.CASCADE)
    rights = models.CharField(
        verbose_name='Права сотрудника для работы с дашбордом команды',
        choices=RIGHT,
        max_length=MAX_LENGTH_RIGHTS)

    class Meta:
        verbose_name = 'Права пользователя'
        verbose_name_plural = 'Права пользователей'
        ordering = ('id_employee',)

    def __str__(self):
        return f'У пользователя {self.id_employee} есть право на {self.rights}'




class Team_s_employees(models.Model):
    """Модель Team's employees (Данные о сотрудниках в командах)."""

    REQUIRED_FIELDS = ['id_employee', 'id_team']

    id_employee = models.ForeignKey(Employee,
                                    verbose_name='Идентификатор сотрудника',
                                    related_name='team_s_employees',
                                    on_delete=models.CASCADE)
    id_team = models.ForeignKey(Team,
                                verbose_name='Идентификатор команды',
                                related_name='team_s_employees',
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Состав команды'
        verbose_name_plural = 'Состав команд'
        ordering = ('id_team',)

    def __str__(self):
        return f'В команде {self.id_team} есть сотрудник(и) {self.id_employee}'


class Team_s_skills(models.Model):
    """Модель Team's skills (Данные о навыках команды)."""

    REQUIRED_FIELDS = ['id_team', 'id_skill', 'key_skill',
                       'required_level', 'required_count_employees']

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
                      'которые должны обладать навыком'))

    class Meta:
        verbose_name = 'Навыки команды'
        verbose_name_plural = 'Навыки команд'
        ordering = ('id_team',)

    def __str__(self):
        return f'У команды {self.id_team} есть навыки {self.id_skill}'


class Employee_skills(models.Model):
    """Модель Employee_skill (Данные о навыках сотрудников)."""

    REQUIRED_FIELDS = ['id_employee', 'id_skill', 'level',
                       'status', 'update_time']
    id_employee = models.ForeignKey(Employee,
                                    verbose_name='Идентификатор сотрудника',
                                    related_name='employee_skills',
                                    on_delete=models.CASCADE)
    id_skill = models.ForeignKey(Skill,
                                 verbose_name='Идентификатор навыка',
                                 related_name='employee_skills',
                                 on_delete=models.CASCADE)
    level = models.CharField(verbose_name='Уровень владения навыком',
                             choices=LEVEL,
                             max_length=MAX_LENGTH_LEVEL)
    status = models.CharField(verbose_name='Статус развития навыка',
                              choices=STATUS,
                              max_length=MAX_LENGTH_STATUS)
    update_date = models.DateTimeField(
        'Дата изменения уровня владения навыком',
        auto_now_add=True)

    class Meta:
        verbose_name = 'Навык сотрудника'
        verbose_name_plural = 'Навыки сотрудников'
        ordering = ('id',)

    def __str__(self):
        return f'У сотрудника {self.id_employee} есть навыки {self.id_skill}'


class Skill_for_grade(models.Model):
    """Модель Skill_for_grade (Данные о навыках для грейда)."""

    REQUIRED_FIELDS = ['id_skill', 'grade', 'required_level_for_grade']

    id_skill = models.ForeignKey(Skill,
                                 verbose_name='Идентификатор навыка',
                                 related_name='skill_for_grades',
                                 on_delete=models.CASCADE)
    grade = models.CharField(verbose_name='Идентификатор грейда сотрудника',
                             choices=GRADE,
                             max_length=MAX_LENGTH_GRADE)
    required_level_for_grade = models.CharField(
        verbose_name='Необходимый уровень для повышения',
        max_length=MAX_LENGTH_REQ_LEVEL_GRADE)

    class Meta:
        verbose_name = 'Навык для грейда'
        verbose_name_plural = 'Навыки для грейда'
        ordering = ('id_skill',)

    def __str__(self):
        return (f'Для грейда {self.grade}'
                f'необходим навык под номером {self.id_skill}')