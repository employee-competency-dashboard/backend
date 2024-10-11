from django.db import models

from users_skills.constants import (MAX_LENGTH_ABOUT_TEAM,
                                    MAX_LENGTH_FIRSTNAME,
                                    MAX_LENGTH_GRADE,
                                    MAX_LENGTH_KEY_EMPLOYEE,
                                    MAX_LENGTH_KEY_SKILL,
                                    MAX_LENGTH_LASTNAME,
                                    MAX_LENGTH_LEVEL,
                                    MAX_LENGTH_NAME_EXPERTISE,
                                    MAX_LENGTH_REQUIRED_LEVEL,
                                    MAX_LENGTH_REQ_LEVEL_GRADE,
                                    MAX_LENGTH_RIGHTS,
                                    MAX_LENGTH_ROLE,
                                    MAX_LENGTH_SKILL_NAME,
                                    MAX_LENGTH_SKILL_TYPE,
                                    MAX_LENGTH_STATUS,
                                    MAX_LENGTH_URL_CONFLUENCE,
                                    MAX_LENGTH_URL_JIRA,
                                    GRADE, LEVEL, RIGHT, SKILL_TYPE,
                                    STATUS)


class Expertise(models.Model):
    """Модель Expertise (Данные о компетенциях)."""

    REQUIRED_FIELDS = ['name_expertise']

    name_expertise = models.CharField(
        verbose_name='Название компетенции',
        max_length=MAX_LENGTH_NAME_EXPERTISE)

    class Meta:
        verbose_name = 'Компетенция'
        verbose_name_plural = 'Компетенции'
        ordering = ('name_expertise',)

    def __str__(self):
        return self.name_expertise


class Skill(models.Model):
    """Модель Skill (Данные о навыках)."""

    REQUIRED_FIELDS = ['skill_name', 'skill_type', 'id_expertise',
                       'grade', 'required_level_for_grade']

    skill_name = models.CharField(
        verbose_name='Название навыка',
        max_length=MAX_LENGTH_SKILL_NAME)
    skill_type = models.CharField(verbose_name='Тип навыка',
                                  choices=SKILL_TYPE,
                                  max_length=MAX_LENGTH_SKILL_TYPE)
    id_expertise = models.ForeignKey(Expertise,
                                     verbose_name='Идентификатор компетенции',
                                     related_name='skills',
                                     on_delete=models.CASCADE)
    grade = models.CharField(verbose_name='Идентификатор грейда сотрудника',
                             choices=GRADE,
                             max_length=MAX_LENGTH_GRADE)
    required_level_for_grade = models.CharField(
        verbose_name='Необходимый уровень для повышения',
        max_length=MAX_LENGTH_REQ_LEVEL_GRADE)

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'
        ordering = ('skill_name',)

    def __str__(self):
        return self.skill_name


class Employee(models.Model):
    """Модель Employee (Данные о сотрудниках)."""

    REQUIRED_FIELDS = ['firstName', 'lastName', 'role',
                       'grade', 'key_employee', 'icon',
                       'rights', 'id_skill', 'level',
                       'status', 'update_time']

    firstName = models.CharField(verbose_name='Имя сотрудника',
                                 max_length=MAX_LENGTH_FIRSTNAME)
    lastName = models.CharField(verbose_name='Фамилия сотрудника',
                                max_length=MAX_LENGTH_LASTNAME)
    role = models.CharField(
        verbose_name='Роль сотрудника в команде (должность)',
        max_length=MAX_LENGTH_ROLE)
    grade = models.CharField(verbose_name='Идентификатор грейда сотрудника',
                             choices=GRADE,
                             max_length=MAX_LENGTH_GRADE)
    key_employee = models.BooleanField(
        verbose_name='Является ли сотрудник ключевым',
        max_length=MAX_LENGTH_KEY_EMPLOYEE)
    icon = models.ImageField(verbose_name='Ссылка на иконку сотрудника',
                             upload_to='users/images/',
                             null=True)
    rights = models.CharField(
        verbose_name='Права сотрудника для работы с дашбордом команды',
        choices=RIGHT,
        max_length=MAX_LENGTH_RIGHTS)
    id_skill = models.ForeignKey(Skill,
                                 verbose_name='Идентификатор навыка',
                                 related_name='employees',
                                 on_delete=models.SET_NULL)
    level = models.CharField(verbose_name='Уровень владения навыком',
                             choices=LEVEL,
                             max_length=MAX_LENGTH_LEVEL)
    status = models.CharField(verbose_name='Статус развития навыка',
                              choices=STATUS,
                              max_length=MAX_LENGTH_STATUS)
    update_time = models.DateTimeField(
        'Дата изменения уровня владения навыком',
        null=True,
        blank=False)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ('lastName',)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'


class Team(models.Model):
    """Модель Team (Данные о команде)."""

    REQUIRED_FIELDS = ['about_team', 'url_confluence', 'url_jira',
                       'team_lead', 'product_owner', 'id_skill',
                       'key_skill', 'required_level',
                       'required_count_employees']

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
    id_skill = models.ForeignKey(Skill,
                                 verbose_name='Идентификатор навыка',
                                 related_name='teams_skill',
                                 null=True,
                                 on_delete=models.SET_NULL)
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
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'
        ordering = ('id',)

    def __str__(self):
        return f'Номер команды: {self.id}'


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
                                null=True,
                                on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Состав команды'
        verbose_name_plural = 'Состав команд'
        ordering = ('id_team',)

    def __str__(self):
        return f'В команде {self.id_team} есть сотрудник(и) {self.id_employee}'
