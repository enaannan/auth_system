from django.urls import path

from users.Views.LoginView import LoginView
from users.Views.MeView import MeView
from users.Views.RefreshToken import CustomTokenRefreshView
from users.Views.RegisterView import RegisterView

urlpatterns = [
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name= 'register'),
    path('login/', LoginView.as_view(), name= 'login'),
    path('me/', MeView.as_view(), name= 'me'),
]