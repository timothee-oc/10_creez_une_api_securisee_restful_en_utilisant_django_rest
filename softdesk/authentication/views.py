from rest_framework import viewsets, permissions
from .models import User
from .serializers import UserSerializer

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [permissions.AllowAny]
        return super().get_permissions()
