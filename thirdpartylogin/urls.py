from django.urls import path

from thirdpartylogin.views import FacebookLogin

urlpatterns = [
    path('facebook/', FacebookLogin.as_view(), name='fb_login'),
]
