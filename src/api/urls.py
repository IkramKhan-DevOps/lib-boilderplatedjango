from django.urls import include, path, re_path
from .docs import get_swagger_doc_schema_view

app_name = 'api'
urlpatterns = []

""" TO LEARN SWAGGER - https://drf-yasg.readthedocs.io/en/stable/readme.html --------------------------------------- """
schema_view = get_swagger_doc_schema_view()
urlpatterns += [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

""" MAIN URLS ------------------------------------------------------------------------------------------------------ """
urlpatterns += [
    re_path('auth/registration/', include('dj_rest_auth.registration.urls')),
    re_path('auth/', include('dj_rest_auth.urls')),
]

""" Version 1 of the API ------------------------------------------------------------------------------------------- """
urlpatterns += [
    path('v1/', include('src.api.v1.urls', namespace='v1')),
]
