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
from django.shortcuts import render
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.static import serve
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from core.config import (
    APP_NAME, APP_DESC, APP_VERSION, APP_TERMS, APP_CONTACT, APP_LICENSE
)
from core.settings import ENVIRONMENT, MEDIA_ROOT, STATIC_ROOT


def handler404(request, *args, **kwargs):
    return render(request, "404.html")


def handler500(request, *args, **kwargs):
    return render(request, "500.html")


handler404 = handler404
handler500 = handler500


""" TO LEARN SWAGGER - https://drf-yasg.readthedocs.io/en/stable/readme.html """
schema_view = get_schema_view(
    openapi.Info(
        title=APP_NAME,
        default_version=APP_VERSION,
        description=APP_DESC,
        terms_of_service=APP_TERMS,
        contact=openapi.Contact(email=APP_CONTACT),
        license=openapi.License(name=APP_LICENSE),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# EXTERNAL APPS URLS
urlpatterns = [

    # DJANGO URLS > remove in extreme security
    path('admin/', admin.site.urls),

    # API URLS
    path('accounts/', include('allauth.urls')),

    # SWAGGER
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # REST-AUTH URLS
    re_path('rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    re_path('rest-auth/', include('dj_rest_auth.urls')),
]

# universal urls
urlpatterns += [
    path('under-construction/', TemplateView.as_view(template_name='under-construction.html')),  # use: for page under-construction

    # REMOVE THIS WHEN HOME VIEW CREATED
    path('', TemplateView.as_view(template_name='dev/starter-page.html')),  # use: for home page/remove this
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
]

# your apps urls
urlpatterns += [
    # path('', include('src.website.urls', namespace='website')),
    path('accounts/', include('src.accounts.urls', namespace='accounts')),
    path('admins/', include('src.administration.admins.urls', namespace='admins')),
]

if ENVIRONMENT != 'server':
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls"))
    ]
