from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenRefreshView


class CustomTokenRefreshView(TokenRefreshView):
    permission_classes = [AllowAny]