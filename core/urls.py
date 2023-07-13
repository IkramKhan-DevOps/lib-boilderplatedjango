from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include, re_path
from django.views.static import serve

from core.settings import ENVIRONMENT, MEDIA_ROOT, STATIC_ROOT


def handler404(request, *args, **kwargs):
    return render(request, "404.html")


def handler500(request, *args, **kwargs):
    return render(request, "500.html")


handler404 = handler404
handler500 = handler500

# EXTERNAL APPS URLS ---------------------------------------------------------------------------------------------------
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('src.accounts.urls', namespace='accounts')),
    path('accounts/', include('allauth.urls')),
]

# DJANGO REST-FRAMEWORK URLS -------------------------------------------------------------------------------------------
urlpatterns += [
    # re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # REST-AUTH URLS
    # re_path('rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    # re_path('rest-auth/', include('dj_rest_auth.urls')),
]

# MEDIA AND STATIC FILES URLS ------------------------------------------------------------------------------------------
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
]

# APPLICATIONS URLS ----------------------------------------------------------------------------------------------------
urlpatterns += [
    path('admins/', include('src.administration.admins.urls', namespace='admins')),
]

# DEVELOPMENT ONLY -----------------------------------------------------------------------------------------------------
if ENVIRONMENT != 'server':
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls"))
    ]
