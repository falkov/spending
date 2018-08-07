# from django.contrib.auth.models import User
from django import forms
from app_add2appauth.models import PasswordForEmail


class PasswordForEmailForm(forms.ModelForm):
    class Meta:
        model = PasswordForEmail
        fields = ('email', 'password_for_email')



