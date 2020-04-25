from django.db import models
from thirdpartylogin.models import CustomUser


class Speciality(models.Model):
    speciality = models.CharField(max_length=250)

    objects = models.Manager()

    def __init__(self, speciality, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.speciality = speciality


class Doctor(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    clinic = models.CharField(max_length=250)
    phone = models.IntegerField()
    picture = models.ImageField()

    objects = models.Manager()

    def __init__(self, user_id, speciality, clinic, phone, picture, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.user_id = user_id
        self.speciality = speciality
        self.clinic = clinic
        self.phone = phone
        self.picture = picture
