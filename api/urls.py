from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)
from .views import ExpertiseViewSet # , SkillViewSet

router = DefaultRouter()
router.register(r'expertises', ExpertiseViewSet)
# router.register(r'expertises', SkillViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'v1/schema/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger'
    ),
    path(
        'v1/schema/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc'
    ),       
]
