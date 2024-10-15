from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from api.serializers import (EmployeeSerializer, Employee_skillsSerializer,
                             ExpertiseSerializer, SkillSerializer, 
                             Skill_for_gradeSerializer, TeamSerializer,
                             Team_s_employeesSerializer,
                             Team_s_skillsSerializer,
                             User_s_teamsSerializer)
from users_skills.models import (Employee, Employee_skills, Expertise,
                                 Skill, Skill_for_grade, Team,
                                 Team_s_employees, Team_s_skills, User_s_teams)


class ExpertiseViewSet(ModelViewSet):
    """Вьюсет для модели Expertise."""

    http_method_names = ['get']
    queryset = Expertise.objects.all()
    serializer_class = ExpertiseSerializer


class Employee_last_nameViewSet(ModelViewSet):
    """Вьюсет для модели Employee."""

    http_method_names = ['get']

    def list(self, request):
        employee_names = Employee.objects.values_list('last_name', flat=True)
        return Response(employee_names)


class Employee_roleViewSet(ModelViewSet):
    """Вьюсет для модели Employee."""

    http_method_names = ['get']

    def list(self, request):
        employee_roles = Employee.objects.values_list('role', flat=True)
        return Response(employee_roles)


class Employee_skillsViewSet(ModelViewSet):
    """Вьюсет для модели Employee_skills."""

    http_method_names = ['get']
    queryset = Employee_skills.objects.all()
    serializer_class = Employee_skillsSerializer


class SkillViewSet(ModelViewSet):
    """Вьюсет для модели Skill."""

    http_method_names = ['get']
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class Skill_for_gradeViewSet(ModelViewSet):
    """Вьюсет для модели Skill_for_grade."""

    http_method_names = ['get']
    queryset = Skill_for_grade.objects.all()
    serializer_class = Skill_for_gradeSerializer


class TeamViewSet(ModelViewSet):
    """Вьюсет для модели Team."""

    http_method_names = ['get']
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class Team_s_employeesViewSet(ModelViewSet):
    """Вьюсет для модели Team_s_employees."""

    http_method_names = ['get']
    queryset = Team_s_employees.objects.all()
    serializer_class = Team_s_employeesSerializer


class Team_s_skillsViewSet(ModelViewSet):
    """Вьюсет для модели Team_s_skills."""

    http_method_names = ['get']
    queryset = Team_s_skills.objects.all()
    serializer_class = Team_s_skillsSerializer


class User_s_teamsViewSet(ModelViewSet):
    """Вьюсет для модели User_s_teams."""

    http_method_names = ['get']
    queryset = User_s_teams.objects.all()
    serializer_class = User_s_teamsSerializer
