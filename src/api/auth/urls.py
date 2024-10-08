from django.urls import path, re_path, include

from dj_rest_auth.views import (
    LogoutView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView,
)
from .views import (
    UserRetrieveChangeAPIView, CustomLoginView, DeactivateUserAPIView, DeleteUserAPIView, GoogleLogin, GoogleConnect,
    AppleLogin, AppleConnect
)

app_name = 'auth'
urlpatterns = [
    path('profile/', UserRetrieveChangeAPIView.as_view(), name='user_retrieve_update'),
    path('login/', CustomLoginView.as_view(), name='rest_login'),
    path('logout/', LogoutView.as_view(), name='rest_logout'),
    path('password/change/', PasswordChangeView.as_view(), name='rest_password_change'),
    path('password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    re_path(r'^password/reset/confirm/$', PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),
    re_path('registration/', include('dj_rest_auth.registration.urls')),
    path('deactivate/', DeactivateUserAPIView.as_view(), name='deactivate'),
    path('delete/', DeleteUserAPIView.as_view(), name='deactivate'),

]

#  Social Auth
urlpatterns += [

    path('google/', GoogleLogin.as_view(), name='google_login'),
    path('google-connect/', GoogleConnect.as_view(), name='google_connect'),
    path('apple/', AppleLogin.as_view(), name='apple_login'),
    path('apple-connect/', AppleConnect.as_view(), name='apple_connect'),
]
