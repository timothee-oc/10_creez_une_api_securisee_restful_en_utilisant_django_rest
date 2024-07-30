from rest_framework import permissions
from .models import Project, Issue

class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

class IsProjectAuthorForIssue(permissions.BasePermission):
    def has_permission(self, request, view):
        project_id = view.kwargs.get("project_pk")
        project = Project.objects.get(id=project_id)
        return project.author == request.user

class IsIssueAuthorForComment(permissions.BasePermission):
    def has_permission(self, request, view):
        issue_id = view.kwargs.get("issue_pk")
        issue = Issue.objects.get(id=issue_id)
        return issue.author == request.user