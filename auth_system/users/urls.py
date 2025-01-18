from django.urls import path

from auth_system.users.Views.LoginView import LoginView
from auth_system.users.Views.MeView import MeView
from auth_system.users.Views.RegisterView import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name= 'register'),
    path('login/', LoginView.as_view(), name= 'login'),
    path('me/', MeView.as_view(), name= 'me'),
]