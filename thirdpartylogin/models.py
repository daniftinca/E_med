from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class UserType(models.IntegerChoices):
        DOCTOR = 1
        PATIENT = 2

    type = models.IntegerField(choices=UserType.choices)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = 1
