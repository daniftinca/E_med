import json

from django.forms import model_to_dict
from django.http import HttpResponse
from django.core import serializers

from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

from thirdpartylogin.models import CustomUser


@csrf_exempt
def profile(request):
    if request.method == 'GET':
        if request.user.type == 2:
            user = CustomUser.objects.get(id=request.user.id)
            patient = user.patient
            if patient:
                return HttpResponse(json.dumps(patient))
            else:
                return HttpResponse('user is created but profile is incomplete', status=status.HTTP_206_PARTIAL_CONTENT)
