from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.apple.views import AppleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView, SocialConnectView
from root.settings import DOMAIN

GOOGLE_CALLBACK_ADDRESS = "accounts/google/login/callback/"
APPLE_CALLBACK_ADDRESS = "accounts/apple/login/callback/"


class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    callback_url = f'{DOMAIN}/{GOOGLE_CALLBACK_ADDRESS}'
    client_class = OAuth2Client

class GoogleConnect(SocialConnectView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = f'{DOMAIN}/{GOOGLE_CALLBACK_ADDRESS}'
    client_class = OAuth2Client

class AppleLogin(SocialLoginView):
    adapter_class = AppleOAuth2Adapter
    callback_url = f'{DOMAIN}/{APPLE_CALLBACK_ADDRESS}'
    client_class = OAuth2Client

class AppleConnect(SocialConnectView):
    adapter_class = AppleOAuth2Adapter
    callback_url = f'{DOMAIN}/{APPLE_CALLBACK_ADDRESS}'
    client_class = OAuth2Client

