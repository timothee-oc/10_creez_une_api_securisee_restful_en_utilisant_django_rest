from rest_framework import viewsets
from .models import Project, Issue, Comment
from .serializers import ProjectSerializer, IssueSerializer, CommentSerializer
from .permissions import IsAuthor, IsProjectAuthorForIssue

class ProjectViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        if self.action in ("update", "partial_update", "destroy"):
            self.permission_classes = [IsAuthor]
        return super().get_permissions()

class IssueViewset(viewsets.ModelViewSet):
    serializer_class = IssueSerializer

    def get_queryset(self):
        project_id = self.kwargs.get("project_pk")
        return Issue.objects.filter(project_id=project_id)

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [IsProjectAuthorForIssue]
        return super().get_permissions()

class CommentViewset(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

