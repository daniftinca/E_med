from django.db import models

# Create your models here.
from consult.models import Consult


class Symptom(models.Model):
    consult = models.ManyToManyField(Consult)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    parent_symptom = models.ForeignKey('self', null=True, related_name='children', on_delete=models.CASCADE)

    objects = models.Manager()

    def __init__(self, name, description, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.name = name
        self.description = description
