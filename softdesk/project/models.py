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