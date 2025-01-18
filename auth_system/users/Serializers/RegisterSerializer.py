from django.contrib.auth import get_user_model

from auth_system.users.models import CustomUser


class RegisterSerializer:
    class Meta:
        model = get_user_model()
        fields=['username','email','password']

    def create(self, validated_data ):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
