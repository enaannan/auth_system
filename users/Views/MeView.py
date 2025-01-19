from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.Serializers.UserSerializer import UserSerilaizer


class MeView(views.APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_description="Retrieve the authenticated user's information",
        security=[{'Bearer': []}]
    )

    def get(self,request):
        serializer = UserSerilaizer(request.user)
        return Response(serializer.data,  status.HTTP_200_OK)