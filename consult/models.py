from django.db import models

# Create your models here.
from thirdpartylogin.models import CustomUser


class Consult(models.Model):
    patient = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='patients_requests_created',
    )
    doctor = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='doctors_requests_created',
    )
    date = models.CharField(max_length=50)
    problem_description = models.CharField(max_length=250)

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('InWork', 'InWork'),
        ('Done', 'Done'),
    ]
    status = models.CharField(
        max_length=250,
        choices=STATUS_CHOICES,
        default='Pending',
    )

    objects = models.Manager()

    def __init__(self, date, problem_description, status, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.date = date
        self.problem_description = problem_description
        self.status = status
