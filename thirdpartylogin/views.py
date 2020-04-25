from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login
# Create your views here.
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from rest_auth.social_serializers import TwitterLoginSerializer

from thirdpartylogin.forms import RegisterForm
from thirdpartylogin.models import CustomUser


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'registration/registration.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if CustomUser.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif CustomUser.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = CustomUser.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                # user.first_name = form.cleaned_data['first_name']
                # user.last_name = form.cleaned_data['last_name']
                # user.phone_number = form.cleaned_data['phone_number']
                user.save()

                # Login the user
                login(request, user)

                # redirect to accounts page:
                return HttpResponseRedirect('/accounts/login')

    # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})