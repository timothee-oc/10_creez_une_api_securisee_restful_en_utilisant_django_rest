from rest_framework.serializers import ModelSerializer
from .models import Contributor

class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ["id", "user", "project", "created_time"]