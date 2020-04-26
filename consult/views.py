from django.shortcuts import render

# Create your views here.
import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from rest_framework import status

from consult.models import Consult
from symptom.models import Symptom
from comment.models import Comment
from thirdpartylogin.models import CustomUser


@csrf_exempt
def consult(request):
    if request.method == 'GET':
        user = CustomUser.objects.get(id=request.user.id)
        user_consult = user.consult
        if user_consult:
            return HttpResponse(user_consult.to_json())
        else:
            return HttpResponse('user is created but profile is incomplete', status=status.HTTP_206_PARTIAL_CONTENT)
    if request.method == 'POST':
        consult_data = json.loads(request.body)
        patient = CustomUser.objects.get(id=consult_data['patient'])
        doctor = CustomUser.objects.get(id=consult_data['doctor'])
        user_consult = Consult(consult_data['date'], consult_data['problem_description'],
                               consult_data['status'])
        user_consult.patient = patient
        user_consult.doctor = doctor
        user_consult.save()
        return HttpResponse(user_consult, status=status.HTTP_201_CREATED)
    return HttpResponse('create doctor profile failed', status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def consult_symptoms(request):
    if request.method == 'GET':
        consult_data = json.loads(request.body)
        symptoms = Symptom.objects.filter(consult__id=consult_data['id'])
        return HttpResponse(serializers.serialize('json', symptoms), status=status.HTTP_200_OK)
    if request.method == 'POST':
        symptom_data = json.loads(request.body)
        user_symptom = Symptom.objects.get(id=symptom_data['symptom'])
        user_symptom.consult.add(symptom_data['consult'])
        user_symptom.save()
        return HttpResponse("symptom created", status=status.HTTP_201_CREATED)
    return HttpResponse('retrieving symptoms profile failed', status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def consult_comment(request):
    if request.method == 'GET':
        consult_data = json.loads(request.body)
        comments = Comment.objects.filter(id=consult_data['id'])
        return HttpResponse(serializers.serialize('json', comments), status=status.HTTP_200_OK)
    if request.method == 'POST':
        consult_data = json.loads(request.body)
        user_consult = Consult.objects.get(id=consult_data['consult'])
        user = CustomUser.objects.get(id=consult_data['user'])
        comment = Comment(consult_data['text'])
        comment.consult = user_consult
        comment.user = user
        comment.save()
        return HttpResponse("symptom created", status=status.HTTP_201_CREATED)
    return HttpResponse('retrieving symptoms profile failed', status=status.HTTP_400_BAD_REQUEST)
