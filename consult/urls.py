from django.urls import path

from . import views

urlpatterns = [
    path('', views.consult, name='consult'),
    path('symptom', views.consult_symptoms, name='consult_symptoms'),
    path('comment', views.consult_comment, name='consult_comment')
]
