import json
from functools import singledispatch
from json import JSONEncoder

from django.core import serializers
from django.db.models.functions import datetime
from django.http import HttpResponse, JsonResponse
import datetime
from django.core.serializers.json import DjangoJSONEncoder

from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

from patientprofile.models import Patient
from thirdpartylogin.models import CustomUser


@csrf_exempt
def patient(request):
    if request.method == 'POST':
        patient_data = json.loads(request.body)
        user = CustomUser.objects.get(id=patient_data['user'])
        user.type = 2
        patient_profile = Patient(patient_data['address'], patient_data['phone'], patient_data['date_of_birth'],
                                  patient_data['picture'], patient_data['health_care_number'])
        patient_profile.user = user
        patient_profile.save()
        return HttpResponse(json.dumps(patient_data), status=status.HTTP_201_CREATED)
    return HttpResponse('something', status=status.HTTP_400_BAD_REQUEST)
