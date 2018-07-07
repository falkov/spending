from django.shortcuts import render

import requests
import socket


# IP = '37.193.167.223'
# IP = '87.117.46.23'
IP = '141.8.144.95 '
# IP = '127.0.0.1'


# Create your views here.
def home(request):

    # r_json = requests.get(f'http://api.sypexgeo.net/json/{IP}').json()
    # r_str = f"{r_json['ip']} - {r_json['city']['name_en']} - {r_json['country']['name_en']} ({r_json['city']['name_en']})"
    # print(r_str)

    # try:
    #     print(socket.getfqdn(IP))  # hostname
    # except Exception as err:
    #     print(err)




    return render(request, 'app_main/home.html', {})
