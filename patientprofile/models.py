from django.db import models


# Create your models here.
from thirdpartylogin.models import CustomUser


class Patient(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    phone = models.IntegerField()
    date_of_birth = models.DateField()
    picture = models.ImageField()
    health_care_number = models.IntegerField()
