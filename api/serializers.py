from drf_extra_fields.fields import Base64ImageField
from rest_framework.serializers import (ModelSerializer,
                                        PrimaryKeyRelatedField,
                                        SerializerMethodField)

from users_skills.constants import (MAX_LENGTH_RIGHTS, RIGHT)
from users_skills.models import (Employee, Expertise, Team,
                                 Skill, Team_s_employees)


class ExpertiseSerializer(ModelSerializer):
    """Сериализатор для модели Expertise."""

    id_expertise = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Expertise
        fields = ('id_expertise', 'name_expertise')


class SkillSerializer(ModelSerializer):
    """Сериализатор для модели Skill."""

    id_skill = PrimaryKeyRelatedField(read_only=True)
    required_level_for_grade = SerializerMethodField(
        method_name='get_required_level_for_grade')

    class Meta:
        model = Skill
        fields = ('id_skill', 'skill_name', 'skill_type', 'id_expertise',
                  'grade', 'required_level_for_grade')
        read_only_fields = ('is_subscribed',)

    def get_required_level_for_grade(self, obj):
        pass


class EmployeeSerializer(ModelSerializer):
    """Сериализатор для модели Employee."""

    id_employee = PrimaryKeyRelatedField(read_only=True)
    id_skill = SkillSerializer(read_only=True)
    icon = Base64ImageField(allow_null=True)

    class Meta:
        model = Employee
        fields = ('id_employee', 'firstName', 'lastName', 'role',
                  'grade', 'key_employee', 'icon',
                  'rights', 'id_skill', 'level',
                  'status', 'update_time')


class TeamSerializer(ModelSerializer):
    """Сериализатор для модели Team."""

    id_team = PrimaryKeyRelatedField(read_only=True)
    id_skill = SkillSerializer(read_only=True)
    team_lead = EmployeeSerializer(read_only=True)
    product_owner = EmployeeSerializer(read_only=True)

    class Meta:
        model = Team
        fields = ('id_team', 'about_team', 'url_confluence', 'url_jira',
                  'team_lead', 'product_owner', 'id_skill',
                  'key_skill', 'required_level', 'required_count_employees')


class Team_s_employeesSerializer(ModelSerializer):
    """Сериализатор для модели Team_s_employees."""

    id = PrimaryKeyRelatedField(read_only=True)
    id_employee = EmployeeSerializer(read_only=True)
    id_team = TeamSerializer(read_only=True)

    class Meta:
        model = Team_s_employees
        fields = ('id', 'id_employee', 'id_team')
