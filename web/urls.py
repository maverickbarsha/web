from idlelib import search

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from web import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
# if settings.DEBUG:
#     urlpatterns= urlpatterns + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
#     urlpatterns= urlpatterns + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
