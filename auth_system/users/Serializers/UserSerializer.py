from django.contrib.auth import get_user_model

class UserSerilaizer:
    class Meta:
        model = get_user_model()
        fields = ['id','username','email']

