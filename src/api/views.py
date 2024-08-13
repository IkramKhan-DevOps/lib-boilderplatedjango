from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.apple.views import AppleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView, SocialConnectView



class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'http://127.0.0.1:8000/accounts/google/login/callback/'
    client_class = OAuth2Client

class GoogleConnect(SocialConnectView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'http://127.0.0.1:8000/accounts/google/login/callback/'
    client_class = OAuth2Client

class AppleLogin(SocialLoginView):
    adapter_class = AppleOAuth2Adapter
    callback_url = 'http://127.0.0.1:8000/accounts/apple/login/callback/'
    client_class = OAuth2Client

class AppleConnect(SocialConnectView):
    adapter_class = AppleOAuth2Adapter
    callback_url = 'http://127.0.0.1:8000/accounts/apple/login/callback/'
    client_class = OAuth2Client

