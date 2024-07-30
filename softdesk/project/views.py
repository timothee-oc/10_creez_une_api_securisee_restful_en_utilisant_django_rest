from rest_framework import viewsets
from .models import Project, Issue, Comment
from .serializers import ProjectSerializer, IssueSerializer, CommentSerializer
from .permissions import IsAuthor, IsProjectAuthorForIssue, IsIssueAuthorForComment

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
        elif self.action in ("update", "partial_update", "destroy"):
            self.permission_classes = [IsAuthor]
        return super().get_permissions()

class CommentViewset(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        issue_id = self.kwargs.get("issue_pk")
        project_id = self.kwargs.get("project_pk")
        return Comment.objects.filter(issue_id=issue_id, issue__project_id=project_id)

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [IsIssueAuthorForComment]
        elif self.action in ("update", "partial_update", "destroy"):
            self.permission_classes = [IsAuthor]
        return super().get_permissions()

