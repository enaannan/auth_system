from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Auth System API",
        default_version='v1',
        description="API documentation for Auth System project",
        contact=openapi.Contact(email="enaannan@gmail.com"),
    ),
    public=True,
)

urlpatterns = [
    path('users/', include('users.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
