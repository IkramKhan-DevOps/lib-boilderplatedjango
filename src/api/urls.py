from django.urls import include, re_path,path
from rest_framework import permissions

from src.api.views import FaceBookLogin
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="API documentation",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
app_name = "api"
urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),    re_path('rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path('rest-auth/', include('rest_auth.urls')),
    re_path('rest-auth/facebook/$', FaceBookLogin.as_view(), name='fb_login'),
]
