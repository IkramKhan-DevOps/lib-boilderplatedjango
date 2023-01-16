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
