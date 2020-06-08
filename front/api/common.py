from rest_framework.viewsets import ModelViewSet

from front import models
from front.serializers.student import SolutionSerializer


class SolutionViewSet(ModelViewSet):
    serializer_class = SolutionSerializer
    queryset = models.Solution.objects.all()
