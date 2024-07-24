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

    name = models.CharField(max_length=50)
    description = models.TextField()
    type = models.CharField(max_length=20, choices=PROJECT_TYPES)
    created_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Issue(models.Model):
    ISSUE_STATUS = {
        "to_do": "To Do",
        "in_progress": "In Progress",
        "finished": "Finished"
    }
    ISSUE_PRIORITIES = {
        "low": "Low",
        "medium": "Medium",
        "high": "High"
    }
    ISSUE_TAGS = {
        "bug": "Bug",
        "feature": "Feature",
        "task": "Task"
    }

    name = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=ISSUE_STATUS, default="to_do")
    priority = models.CharField(max_length=20, choices=ISSUE_PRIORITIES)
    tag = models.CharField(max_length=20, choices=ISSUE_TAGS)
    created_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class Comment(models.Model):
    description = models.TextField()
    issue_link = models.CharField(max_length=50)
    unique_id = models.UUIDField(default=uuid4)
    created_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
