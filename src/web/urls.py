from django.contrib import admin

from django.urls import path, include

urlpatterns = [
    path('', include('src.web.website.urls', namespace='website')),
    path('accounts/', include('src.web.accounts.urls', namespace='accounts')),
    path('admins/', include('src.web.admins.urls', namespace='admins')),
]