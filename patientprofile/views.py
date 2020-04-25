import json

from django.core import serializers
from django.http import HttpResponse

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
        return HttpResponse(patient_profile.to_json(), status=status.HTTP_201_CREATED)
    return HttpResponse('something', status=status.HTTP_400_BAD_REQUEST)
