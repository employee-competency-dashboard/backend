from django.urls import include, path

from rest_framework.routers import DefaultRouter
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)

from api.views import (Employee_last_nameViewSet,
                       Employee_roleViewSet,
                       Employee_skillsViewSet,
                       ExpertiseViewSet, SkillViewSet,
                       TeamViewSet,
                       Team_s_employeesViewSet,
                       Team_s_skillsViewSet,
                       User_s_teamsViewSet)

v1_router = DefaultRouter()

v1_router.register('access/check', User_s_teamsViewSet,
                   basename='user_s_teams')
v1_router.register('info/team-info', TeamViewSet, basename='teams')
v1_router.register('info/employees-skills', Employee_skillsViewSet,
                   basename='employees_skills')
v1_router.register('filter-list/expertise', ExpertiseViewSet,
                   basename='expertises')
v1_router.register('filter-list/skill', SkillViewSet,
                   basename='skills')
v1_router.register('filter-list/employee-fio', Employee_last_nameViewSet,
                   basename='empployee_names')
v1_router.register('filter-list/employee-role', Employee_roleViewSet,
                   basename='empployee_roles')


urlpatterns = [
    path('', include(v1_router.urls)),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'schema/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger'
    ),
    path(
        'schema/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc'
    )   
]
