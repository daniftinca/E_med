import json

from django.core import serializers
from django.db import models
from thirdpartylogin.models import CustomUser


class Speciality(models.Model):
    speciality = models.CharField(max_length=250)

    objects = models.Manager()

    def __init__(self, speciality, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.speciality = speciality

    def to_json(self):
        data = serializers.serialize('json', [self, ])
        struct = json.loads(data)
        return json.dumps(struct[0])


class Doctor(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        primary_key=True,
        blank=True
    )
    speciality = models.ManyToManyField(Speciality)
    clinic = models.CharField(max_length=250)
    phone = models.IntegerField()
    picture = models.ImageField()

    objects = models.Manager()

    def __init__(self, clinic, phone, picture, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.clinic = clinic
        self.phone = phone
        self.picture = picture

    def to_json(self):
        data = serializers.serialize('json', [self, ])
        struct = json.loads(data)
        return json.dumps(struct[0])
