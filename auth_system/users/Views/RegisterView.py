from rest_framework import status
from rest_framework.response import Response

from auth_system.users import views
from auth_system.users.Serializers import RegisterSerializer


class RegisterView(views.APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"User created successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)