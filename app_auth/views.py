from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from app_auth.forms import UserForm

from allauth.account.forms import SignupForm


# Create your views here.
def sign_up(request):
    print('1---------')

    context = {
        'signup_form': SignupForm
    }
    # user_form = UserForm()

    # return render(request, 'app_auth/signup.html', {'user_form': user_form})
    return render(request, 'app_auth/account/templates/app_auth/signup.html', context)
