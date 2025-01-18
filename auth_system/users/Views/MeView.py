from rest_framework import status, views
from rest_framework.response import Response

from auth_system.users.Serializers.UserSerializer import UserSerilaizer


class MeView(views.APIView):
    def get(self,request):
        serializer = UserSerilaizer(request.user)
        return Response(serializer.data, not status.HTTP_200_OK)