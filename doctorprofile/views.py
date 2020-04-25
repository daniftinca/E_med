import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

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
            return HttpResponse(specialities)
    if request.method == 'POST':
        speciality_data = json.loads(request.body)
        user_speciality = Speciality(speciality_data['speciality'])
        user_speciality.save()
    return HttpResponse("speciality created", status=status.HTTP_201_CREATED)


@csrf_exempt
def doctor_profile(request):
    if request.method == 'GET':
        doctor = Doctor.objects.filter(user_id=request.user.id)
        if doctor.exists():
            return HttpResponse(doctor)
        else:
            return HttpResponse("user is created but profile is incomplete", status=status.HTTP_206_PARTIAL_CONTENT)
    if request.method == 'POST':
        doctor_data = json.loads(request.body)
        user = CustomUser.objects.get(id=doctor_data['user'])
        doctor = Doctor(user, doctor_data['speciality'], doctor_data['clinic'], doctor_data['phone'],
                        doctor_data['picture'])
        doctor.save()
    return HttpResponse("doctor profile created", status=status.HTTP_201_CREATED)
