import json

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

from patientprofile.models import Patient
from thirdpartylogin.models import CustomUser


@csrf_exempt
def profile(request):
    if request.method == 'GET':
        patient = Patient.objects.filter(user_id=request.user.id)
        if patient.exists():
            return HttpResponse(patient)
        else:
            return HttpResponse('user is created but profile is incomplete', status=status.HTTP_206_PARTIAL_CONTENT)
    if request.method == 'POST':
        patient_data = json.loads(request.body)
        user = CustomUser.objects.get(id=patient_data['user'])
        patient = Patient(user, patient_data['address'], patient_data['phone'], patient_data['date_of_birth'],
                          patient_data['picture'], patient_data['health_care_number'])
        patient.save()
        return HttpResponse(tatus=status.HTTP_201_CREATED)
