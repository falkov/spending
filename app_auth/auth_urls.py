from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/',  auth_views.login,  {'template_name': 'app_auth/login.html'}, name='auth-login'),
    path('logout/', auth_views.logout, {'next_page': '/'}, name='auth-logout'),
    path('signup/', views.sign_up, name='auth-signup'),

]
