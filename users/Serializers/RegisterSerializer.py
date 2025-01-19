from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.models import Users


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields=['username','email','password']

    def create(self, validated_data ):
        user = Users.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
