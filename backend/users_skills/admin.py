from django.contrib import admin

from users_skills.models import (Employee, Employee_skills, Expertise,
                                 Skill, Skill_for_grade, Team,
                                 Team_s_employees, Team_s_skills, User_s_teams)


@admin.register(Expertise)
class ExpertiseAdmin(admin.ModelAdmin):
    """Модель ExpertiseAdmin."""

    list_display = ('name_expertise',)
    search_fields = ('name_expertise',)
    list_filter = ('name_expertise',)
    list_display_links = ('name_expertise',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """Модель SkillAdmin."""

    list_display = ('skill_name', 'skill_type', 'id_expertise')
    search_fields = ('skill_name',)
    list_filter = ('skill_name',)
    list_display_links = ('skill_name',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """Модель EmployeeAdmin."""

    list_display = ('first_name', 'last_name', 'role', 'grade',
                    'key_employee', 'icon')
    search_fields = ('last_name',)
    list_filter = ('last_name',)
    list_display_links = ('last_name',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    """Модель TeamAdmin."""

    list_display = ('about_team', 'url_confluence', 'url_jira',
                    'team_lead', 'product_owner')
    search_fields = ('about_team',)
    list_filter = ('about_team',)
    list_display_links = ('about_team',)


@admin.register(Team_s_employees)
class Team_s_employeesAdmin(admin.ModelAdmin):
    """Модель Team_s_employeesAdmin."""

    list_display = ('id_employee', 'id_team')
    search_fields = ('id_team',)
    list_filter = ('id_team',)
    list_display_links = ('id_team',)


@admin.register(User_s_teams)
class User_s_teamsAdmin(admin.ModelAdmin):
    """Модель User_s_teamsAdmin."""

    list_display = ('id_employee', 'id_team', 'rights')
    search_fields = ('id_employee',)
    list_filter = ('id_employee',)
    list_display_links = ('id_employee',)


@admin.register(Team_s_skills)
class Team_s_skillsAdmin(admin.ModelAdmin):
    """Модель Team_s_skillsAdmin."""

    list_display = ('id_team', 'id_skill', 'key_skill',
                    'required_level', 'required_count_employees')
    search_fields = ('id_team',)
    list_filter = ('id_team',)
    list_display_links = ('id_team',)


@admin.register(Skill_for_grade)
class Skill_for_gradeAdmin(admin.ModelAdmin):
    """Модель Skill_for_gradeAdmin."""

    list_display = ('id_skill', 'grade', 'required_level_for_grade')
    search_fields = ('id_skill',)
    list_filter = ('id_skill',)
    list_display_links = ('id_skill',)


@admin.register(Employee_skills)
class Employee_skillsAdmin(admin.ModelAdmin):
    """Модель Employee_skillsAdmin."""

    list_display = ('id_employee', 'id_skill', 'level',
                    'status', 'update_date')
    search_fields = ('id_employee',)
    list_filter = ('id_employee',)
    list_display_links = ('id_employee',)
