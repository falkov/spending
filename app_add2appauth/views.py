from django.shortcuts import render
from django.views.generic import TemplateView

from app_add2appauth.forms import PasswordForEmailForm


def password_for_email(request):
    form = PasswordForEmailForm

    return render(request, 'passwords_for_email.html', {
        'form': form
    })


class PasswordForEmail(TemplateView):
    template_name = 'app_add2appauth/passwords_for_emails.html'

    def get_context_data(self, **kwargs):
        context = super(PasswordForEmail, self).get_context_data(**kwargs)
        context['falkov'] = 'Сергей Фалькович, привет! как дела?'
        context['ip'] = '141.8.144.95'

        return context