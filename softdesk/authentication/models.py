import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_birth_date(value):
    if datetime.date.today() - value < datetime.timedelta(days=15*365):
        raise ValidationError("You need to be at least 15 to sign in")

class User(AbstractUser):
    birth_date = models.DateField(validators=[validate_birth_date])
    can_be_contacted = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)
