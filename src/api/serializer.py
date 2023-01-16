from rest_auth.serializers import LoginSerializer


class MyCustomSerializer(LoginSerializer):
    class Meta:
        fields = [
            'email', 'password'
        ]
