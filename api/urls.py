from django.urls import include, path
from rest_framework import routers 
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView
)
from .views import ExpertiseViewSet # , SkillViewSet

router = routers.DefaultRouter()
router.register(r'expertises', ExpertiseViewSet)
# router.register(r'expertises', SkillViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('', include(router.urls)),
]
