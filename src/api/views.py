from rest_auth.views import LoginView

from src.api.serializer import MyCustomSerializer


class MyLoginView(LoginView):
    serializer_class = MyCustomSerializer
