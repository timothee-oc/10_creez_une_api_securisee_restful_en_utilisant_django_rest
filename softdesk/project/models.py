from uuid import uuid4
from django.db import models
from authentication.models import User


class Project(models.Model):
    PROJECT_TYPES = {
        "backend": "back-end",
        "frontend": "front-end",
        "ios": "iOS",
        "android": "Android"
    }

    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=100, choices=PROJECT_TYPES)
    created_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Issue(models.Model):
    ISSUE_STATUS = {
        "to do": "To Do",
        "in progress": "In Progress",
        "finished": "Finished"
    }
    ISSUE_PRIORITIES = {
        "low": "LOW",
        "medium": "MEDIUM",
        "high": "HIGH"
    }
    ISSUE_TAGS = {
        "bug": "BUG",
        "feature": "FEATURE",
        "task": "TASK"
    }

    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=ISSUE_STATUS, default="To Do")
    priority = models.CharField(max_length=20, choices=ISSUE_PRIORITIES)
    tag = models.CharField(max_length=20, choices=ISSUE_TAGS)
    created_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="assigned_issues")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class Comment(models.Model):
    description = models.TextField()
    unique_id = models.UUIDField(default=uuid4, unique=True, editable=False)
    created_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
