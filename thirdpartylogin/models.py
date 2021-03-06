from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class UserType(models.IntegerChoices):
        DOCTOR = 1
        PATIENT = 2

    type = models.IntegerField(choices=UserType.choices, default=1)
