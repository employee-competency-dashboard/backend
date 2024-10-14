from drf_extra_fields.fields import Base64ImageField
from rest_framework.fields import DateTimeField
from rest_framework.serializers import (ModelSerializer,
                                        PrimaryKeyRelatedField,
                                        SerializerMethodField)

from users_skills.models import (Employee, Employee_skills, Expertise,
                                 Skill, Skill_for_grade, Team,
                                 Team_s_employees, Team_s_skills, User_s_teams)


class ExpertiseSerializer(ModelSerializer):
    """Сериализатор для модели Expertise."""

    id_expertise = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Expertise
        fields = ('id_expertise', 'name_expertise')


class SkillSerializer(ModelSerializer):
    """Сериализатор для модели Skill."""

    id_skill = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Skill
        fields = ('id_skill', 'skill_name', 'skill_type', 'id_expertise')


class EmployeeSerializer(ModelSerializer):
    """Сериализатор для модели Employee."""

    id_employee = PrimaryKeyRelatedField(read_only=True)
    icon = Base64ImageField(allow_null=True)

    class Meta:
        model = Employee
        fields = ('id_employee', 'first_name', 'last_name', 'role', 'grade',
                  'key_employee', 'icon')



class Team_s_employeesSerializer(ModelSerializer):
    """Сериализатор для модели Team_s_employees."""

    employee = EmployeeSerializer(source='id_employee')

    class Meta:
        model = Team_s_employees
        fields = ['id_employee', 'id_team', 'employee']


class TeamSerializer(ModelSerializer):
    """Сериализатор для модели Team."""

    team_lead = EmployeeSerializer(read_only=True)
    product_owner = EmployeeSerializer(read_only=True)
    employees = Team_s_employeesSerializer(source='team_s_employees', many=True, read_only=True)
    class Meta:
        model = Team
        fields = ['about_team', 'url_confluence', 'url_jira',
                  'team_lead', 'product_owner', 'employees']
    


class User_s_teamsSerializer(Team_s_employeesSerializer):
    """Сериализатор для модели User_s_teams."""

    class Meta:
        model = User_s_teams
        fields = ('id', 'id_employee', 'id_team', 'rights')


class Team_s_skillsSerializer(ModelSerializer):
    """Сериализатор для модели Team_s_skills."""

    id_team = TeamSerializer(read_only=True)
    id_skill = SkillSerializer(read_only=True)

    class Meta:
        model = Team_s_skills
        fields = ('id', 'id_team', 'id_skill', 'key_skill',
                  'required_level', 'required_count_employees')


class Skill_for_gradeSerializer(ModelSerializer):
    """Сериализатор для модели Skill_for_grade."""

    id_skill = PrimaryKeyRelatedField(read_only=True)
    required_level_for_grade = SerializerMethodField(
        method_name='get_required_level_for_grade')

    class Meta:
        model = Skill_for_grade
        fields = ('id', 'id_skill', 'grade', 'required_level_for_grade')

    def get_required_level_for_grade(self, obj):
        pass


class Employee_skillsSerializer(ModelSerializer):
    """Сериализатор для модели Employee_skills."""

    id_employee = PrimaryKeyRelatedField(read_only=True)
    id_skill = SkillSerializer(read_only=True)

    class Meta:
        model = Employee_skills
        fields = ('id', 'id_employee', 'id_skill', 'level',
                  'status', 'update_date')
