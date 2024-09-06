from rest_framework import viewsets
from user.models import User
from .models import Project, Contributor, Issue, Comment
from .serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer
from .permissions import IsAuthor, IsContributor

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        project = serializer.save(author=self.request.user)
        Contributor.objects.create(user=self.request.user, project=project, role='AUTHOR', author=self.request.user)

    def get_queryset(self):
        return Project.objects.filter(contributors__user=self.request.user)
    
    def get_permissions(self):
        if self.action == 'create':
            return super().get_permissions()
        return [IsAuthor()]

class ContributorViewSet(viewsets.ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthor, IsContributor]

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_pk')
        project = Project.objects.get(pk=project_id)
        user_id = self.request.data.get('user')
        user = User.objects.get(pk=user_id)
        serializer.save(user=user, project=project, role='CONTRIBUTOR', author=self.request.user)
    
    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        return Contributor.objects.filter(project_id=project_id)

class IssueViewSet(viewsets.ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthor, IsContributor]

    def perform_create(self, serializer):
        project_id = self.kwargs.get('project_pk')
        project = Project.objects.get(pk=project_id)
        serializer.save(author=self.request.user, project=project)
    
    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        return Issue.objects.filter(project_id=project_id)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthor, IsContributor]

    def perform_create(self, serializer):
        issue_id = self.kwargs.get('issue_pk')
        issue = Issue.objects.get(pk=issue_id)
        serializer.save(author=self.request.user, issue=issue)
    
    def get_queryset(self):
        issue_id = self.kwargs.get('issue_pk')
        project_id = self.kwargs.get('project_pk')
        return Comment.objects.filter(issue_id=issue_id, issue__project_id=project_id) # QUESTION
