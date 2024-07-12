from uuid import uuid4
from django.db import models
from authentication.models import User


class Project(models.Model):
    PROJECT_TYPES = {
        "BACKEND": "back-end",
        "FRONTEND": "front-end",
        "IOS": "IOS",
        "ANDROID": "Android"
    }

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=100, choices=PROJECT_TYPES)
    created_time = models.DateTimeField(auto_now_add=True)

class Issue(models.Model):
    ISSUE_STATUS = {
        "TODO": "To Do",
        "INPROGRESS": "In Progress",
        "FINISHED": "Finished"
    }
    ISSUE_PRIORITIES = {
        "LOW": "Low",
        "MEDIUM": "Medium",
        "HIGH": "High"
    }
    ISSUE_TAGS = {
        "BUG": "Bug",
        "FEATURE": "Feature",
        "TASK": "Task"
    }
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=100, choices=ISSUE_STATUS, default=ISSUE_STATUS["TODO"])
    priority = models.CharField(max_length=100, choices=ISSUE_PRIORITIES)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assigned_issues')
    tag = models.CharField(max_length=100, choices=ISSUE_TAGS)
    created_time = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    unique_id = models.UUIDField(default=uuid4, editable=False, unique=True)
    created_time = models.DateTimeField(auto_now_add=True)
