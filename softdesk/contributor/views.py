from rest_framework.viewsets import ModelViewSet
from .models import Contributor
from .serializers import ContributorSerializer

class ContributorViewset(ModelViewSet):
    serializer_class = ContributorSerializer
    queryset = Contributor.objects.all()