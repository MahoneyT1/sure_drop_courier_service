"""
URL configuration for Courier_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


schema_view = get_schema_view(
    openapi.Info(
        title="Courier Service API",
        default_version='v1',
        description="API documentation for the Courier Service application",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

class HealthCheckView(APIView):
    """Health check view to verify if the service is running
    """
    permission_classes = [AllowAny]

    def get(self, request):
        """Handles GET requests for health check
        """
        return Response(
            {"status": "Service is running smoothly."},
            status=status.HTTP_200_OK
        )
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('User.urls')),
    path('api/v1/', include('Package.urls')),
    path('api/v1/', include('Delivery.urls')),
    path('api/v1/', include('Courier.urls')),
    path('api/v1/', include('Location.urls')),
    path('api/v1/', include('Receipt.urls')),
    path('', HealthCheckView.as_view(), name='health-check'),

    # Swagger documentation URLs
    path('api/v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 
]
