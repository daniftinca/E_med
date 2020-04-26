import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from rest_framework import status

from doctorprofile.models import Speciality, Doctor
from thirdpartylogin.models import CustomUser


@csrf_exempt
def speciality(request):
    if request.method == 'GET':
        specialities = Speciality.objects.all()
        if not specialities:
            return HttpResponse("there are no specialities", status=status.HTTP_200_OK)
        else:
            return HttpResponse(serializers.serialize('json', specialities), status=status.HTTP_200_OK)
    if request.method == 'POST':
        speciality_data = json.loads(request.body)
        user_speciality = Speciality(speciality_data['speciality'])
        user_speciality.save()
    return HttpResponse("speciality created", status=status.HTTP_201_CREATED)


@csrf_exempt
def doctor(request):
    if request.method == 'POST':
        doctor_data = json.loads(request.body)
        user = CustomUser.objects.get(id=doctor_data['user'])
        user.type = 1
        doctor_profile = Doctor(doctor_data['clinic'], doctor_data['phone'],
                                doctor_data['picture'])
        # user.save()
        doctor_profile.user = user
        doctor_profile.save()
        doctor_profile.speciality.add(doctor_data['speciality'])
        doctor_profile.save()
        return HttpResponse(doctor_profile.to_json(), status=status.HTTP_201_CREATED)
    return HttpResponse('create doctor profile failed', status=status.HTTP_400_BAD_REQUEST)
