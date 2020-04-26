from django.db import models

# Create your models here.
from consult.models import Consult
from thirdpartylogin.models import CustomUser


class Comment(models.Model):
    consult = models.ForeignKey(
        Consult,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )
    text = models.CharField(max_length=250)
    date = models.DateField()

    objects = models.Manager()

    def __init__(self, text, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.text = text
