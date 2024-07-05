from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator

class User(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=(MinValueValidator(15),))
    can_be_contacted = models.BooleanField(blank=True, default=False)
    can_data_be_shared = models.BooleanField(blank=True, default=False)
    created_time = models.DateTimeField(auto_now_add=True)