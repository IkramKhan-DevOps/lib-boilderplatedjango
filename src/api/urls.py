from django.template.defaulttags import url
from django.urls import include, re_path,path
from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token, verify_jwt_token

app_name = "api"
urlpatterns = [
    re_path('rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path('rest-auth/', include('rest_auth.urls')),
    re_path('api-token-refresh/', refresh_jwt_token),
    re_path(r'^api-token-auth/', obtain_jwt_token),
    re_path(r'^api-token-verify/', verify_jwt_token),
]
