from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('document/meusarquivos',admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

STATIC_ROOT = "/var/www/example.com/static/"
