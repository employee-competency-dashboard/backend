from rest_framework import viewsets
from users_skills.models import Expertise
from .serializers import ExpertiseSerializer


class ExpertiseViewSet(viewsets.ModelViewSet):
    queryset = Expertise.objects.all()
    serializer_class = ExpertiseSerializer
