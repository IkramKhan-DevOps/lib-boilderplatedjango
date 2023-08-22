from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


def get_swagger_doc_schema_view():

    return get_schema_view(
        openapi.Info(
            title='API',
            default_version='v1.0',
            description='Application detailed down api implementation. need help contact exarth.com',
            terms_of_service='https://exarth.com/terms-of-use/',
            contact=openapi.Contact(email='support@exarth.com'),
            license=openapi.License(name='NDA (protected)'),
        ),
        public=True,
        permission_classes=[permissions.AllowAny],
    )
