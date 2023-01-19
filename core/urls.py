"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the admin() function: from django.urls import admin, path
    2. Add a URL to urlpatterns:  path('blog/', admin('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from src.api.views import FaceBookLogin

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="API documentation",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
# CORE URLS
urlpatterns = [

    # SYS URLS > remove in extreme security
    path('admin/', admin.site.urls),

    # API URLS
    path('accounts/', include('allauth.urls')),

    # APPS URLS
    path('api/', include('src.api.urls', namespace='api')),
    path('', include('src.website.urls', namespace='website')),
    path('accounts/', include('src.accounts.urls', namespace='accounts')),
    path('admins/', include('src.administration.admins.urls', namespace='admins')),
]
# UNIVERSAL URLS
urlpatterns += [
    # 404-500-00 PAGES
    path('under-construction/', TemplateView.as_view(template_name='000.html')),
    path('404/', TemplateView.as_view(template_name='404.html')),
    path('500/', TemplateView.as_view(template_name='500.html')),
    # REMOVE THIS WHEN HOME VIEW CREATED
    path('', TemplateView.as_view(template_name='000.html')),
]


# Swagger and Exarth Rest Auth Urls
urlpatterns +=[

    path('rest-auth/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    re_path('rest-auth/registration/', include('exarth_rest_auth.registration.urls')),
    re_path('rest-auth/', include('exarth_rest_auth.urls')),
    re_path('rest-auth/facebook/$', FaceBookLogin.as_view(), name='fb_login'),
]