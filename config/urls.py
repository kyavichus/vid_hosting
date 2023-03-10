from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from video_hosting.views import rate_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('video_hosting.urls')),
    path('users', include('users.urls')),

]


if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
