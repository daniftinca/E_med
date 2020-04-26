from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

from thirdpartylogin.models import CustomUser


@csrf_exempt
def profile(request):
    if request.method == 'GET':
        if request.user.type == 1:
            user = CustomUser.objects.get(id=request.user.id)
            doctor = user.doctor
            if doctor:
                return HttpResponse(doctor.to_json())
            else:
                return HttpResponse('user is created but profile is incomplete', status=status.HTTP_206_PARTIAL_CONTENT)
        if request.user.type == 2:
            user = CustomUser.objects.get(id=request.user.id)
            patient = user.patient
            if patient:
                return HttpResponse(patient.to_json())
            else:
                return HttpResponse('user is created but profile is incomplete', status=status.HTTP_206_PARTIAL_CONTENT)
