from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer

class UserViewset(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()
    
    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [AllowAny]
        return super().get_permissions()