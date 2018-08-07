from django.db import models
from allauth.account.models import EmailAddress

# Create your models here.

class PasswordForEmail(models.Model):
    email = models.OneToOneField(EmailAddress, on_delete=models.CASCADE)
    password_for_email = models.CharField(max_length=30)

    def __str__(self):
        return f"email = {self.email}, password_for_email = {self.password_for_email}"