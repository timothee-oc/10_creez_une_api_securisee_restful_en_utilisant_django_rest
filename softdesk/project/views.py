from rest_framework.viewsets import ModelViewSet
from .models import Project, Issue, Comment
from .serializers import ProjectSerializer, IssueSerializer, CommentSerializer

class ProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class IssueViewset(ModelViewSet):
    serializer_class = IssueSerializer
    queryset = Issue.objects.all()

class CommentViewset(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()