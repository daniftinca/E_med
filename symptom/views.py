from django.shortcuts import render

# Create your views here.

import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from rest_framework import status

from symptom.models import Symptom


@csrf_exempt
def symptom(request):
    if request.method == 'GET':
        user_symptom = Symptom.objects.all()
        # return HttpResponse(serializers.serialize('json', user_symptom), status=status.HTTP_200_OK)
        return HttpResponse(user_symptom, status=status.HTTP_200_OK)
    if request.method == 'POST':
        symptom_data = json.loads(request.body)
        user_symptom = Symptom(symptom_data['name'], symptom_data['description'])
        user_symptom.parent_symptom_id = symptom_data['parent_symptom']
        user_symptom.save()
        return HttpResponse("symptom created", status=status.HTTP_201_CREATED)
