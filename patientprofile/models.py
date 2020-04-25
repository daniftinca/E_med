import json

from django.core import serializers
from django.db import models

# Create your models here.
from thirdpartylogin.models import CustomUser


class Patient(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
    )
    address = models.CharField(max_length=250)
    phone = models.IntegerField()
    date_of_birth = models.DateField()
    picture = models.ImageField()
    health_care_number = models.IntegerField()

    def __init__(self,  address, phone, date_of_birth, picture, health_care_number, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # self.user = user
        self.address = address
        self.phone = phone
        self.date_of_birth = date_of_birth
        self.picture = picture
        self.health_care_number = health_care_number

    def to_json(self):
        data = serializers.serialize('json', [self, ])
        struct = json.loads(data)
        return json.dumps(struct[0])
