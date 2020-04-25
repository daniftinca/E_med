from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

from patientprofile.models import Patient
from thirdpartylogin.models import CustomUser


@csrf_exempt
def profile(request):
    if request.method == 'GET':
        if request.user.type == 1:
            user = CustomUser.objects.get(id=request.user.id)
            patient = user.patient
            if patient:
                return HttpResponse(patient)
            else:
                return HttpResponse('user is created but profile is incomplete', status=status.HTTP_206_PARTIAL_CONTENT)
