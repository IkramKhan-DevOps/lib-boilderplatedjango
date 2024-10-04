from django.urls import include, path, re_path
from .docs import get_swagger_doc_schema_view
from . import views

app_name = 'api'
urlpatterns = []

""" TO LEARN SWAGGER - https://drf-yasg.readthedocs.io/en/stable/readme.html --------------------------------------- """
schema_view = get_swagger_doc_schema_view()
urlpatterns += [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

""" REST AUTH API----------------------------------------------------------------------------------------------------"""
urlpatterns = [
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),


    path('dj-rest-auth/google/', views.GoogleLogin.as_view(), name='google_login'),
    path('dj-rest-auth/google-connect/', views.GoogleConnect.as_view(), name='google_connect'),

    path('dj-rest-auth/apple/', views.AppleLogin.as_view(), name='apple_login'),
    path('dj-rest-auth/apple-connect/', views.AppleConnect.as_view(), name='apple_connect'),

]


""" Version 1 of the API ------------------------------------------------------------------------------------------- """
urlpatterns += [
    path('v1/', include('src.api.v1.urls', namespace='v1')),
]
