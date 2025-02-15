from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    #Paths de la app core
    path('', include('core.urls')),
    #Paths del admin
    path('admin/', admin.site.urls),
]

from django.conf import settings
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)