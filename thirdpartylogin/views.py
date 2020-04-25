from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from django.shortcuts import render

# Create your views here.
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from rest_auth.social_serializers import TwitterLoginSerializer


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
