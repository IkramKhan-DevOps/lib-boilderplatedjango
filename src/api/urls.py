from django.urls import include, path

from src.api.docs import get_swagger_doc_schema_view

app_name = 'api'
urlpatterns = []

""" TO LEARN SWAGGER - https://drf-yasg.readthedocs.io/en/stable/readme.html --------------------------------------- """
schema_view = get_swagger_doc_schema_view()
urlpatterns += [
    path('api/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


""" Version 1 of the API ------------------------------------------------------------------------------------------- """
urlpatterns += [
    path('api/v1/', include('src.api.v1.urls', namespace='v1')),
    path('auth/', include('src.api.auth.urls', namespace='auth')),
]