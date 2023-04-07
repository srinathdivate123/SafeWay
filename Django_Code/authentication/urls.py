from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views as a
urlpatterns = [
    path('registration', csrf_exempt(a.RegistrationView), name = 'reg'),
    path('login', csrf_exempt(a.LoginView), name = 'login'),
    path('logout', csrf_exempt(a.LogoutView), name = 'logout'),
]
