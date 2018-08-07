from django.shortcuts import render
from django.views.generic import TemplateView


import requests
import socket


# IP = '37.193.167.223'
# IP = '87.117.46.23'
IP = '141.8.144.95'
# IP = '127.0.0.1'


class Home(TemplateView):
    template_name = 'app_main/home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['falkov'] = 'Сергей Фалькович, привет! как дела?'
        context['ip'] = IP

        return context
