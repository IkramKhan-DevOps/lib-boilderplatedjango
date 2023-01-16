from django.urls import include, re_path,path
from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token, verify_jwt_token


app_name = "api"
urlpatterns = [
    re_path('rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path('rest-auth/', include('rest_auth.urls')),
]
