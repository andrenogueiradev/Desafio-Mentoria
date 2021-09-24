from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from register.views import ClientViewSet, CompanyViewSet
from rest_framework.authtoken import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'Client', ClientViewSet, basename= 'Client')
router.register(r'Company', CompanyViewSet, basename='Company')


schema_view = get_schema_view(
   openapi.Info(
      title="API Documentation",
      default_version='v1',
      description="Chelder's Challenge",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('document/meusarquivos',admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

STATIC_ROOT = "/var/www/example.com/static/"
