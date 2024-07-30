from rest_framework import permissions
from .models import Project

class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

class IsProjectAuthorForIssue(permissions.BasePermission):
    def has_permission(self, request, view):
        project_id = view.kwargs.get("project_pk")
        project = Project.objects.get(id=project_id)
        return project.author == request.user