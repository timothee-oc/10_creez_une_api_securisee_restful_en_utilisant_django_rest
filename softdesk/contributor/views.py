from rest_framework.viewsets import ModelViewSet
from .models import Contributor
from .serializers import ContributorSerializer

class ContributorViewset(ModelViewSet):
    serializer_class = ContributorSerializer

    def get_queryset(self):
        return Contributor.objects.all()