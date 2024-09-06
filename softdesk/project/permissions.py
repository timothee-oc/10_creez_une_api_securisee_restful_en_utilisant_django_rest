from rest_framework import permissions
from .models import Project, Contributor

class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

class IsContributor(permissions.BasePermission):
    def has_permission(self, request, view):
        project_pk = view.kwargs.get('project_pk')
        try:
            project = Project.objects.get(pk=project_pk)
        except Project.DoesNotExist:
            return False
        return Contributor.objects.filter(project=project, user=request.user).exists()
