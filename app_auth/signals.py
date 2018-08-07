# from django.db import models
from django.contrib.auth.models import User
# from app_fni import views as fni_views
# from app_fni.views import check_mail

from allauth.account import signals
from django.dispatch import receiver


@receiver(signals.user_logged_in, sender=User)
def my_send_login(sender, **kwargs):
    print(f'*** login: {User.username}')

@receiver(signals.user_logged_out, sender=User)
def my_send_logout(sender, **kwargs):
    print(f'*** logout: {User.email}')
