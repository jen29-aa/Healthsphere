# healthsp/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # <-- ADD THIS IMPORT
from django.conf.urls.static import static  # <-- ADD THIS IMPORT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('predict.urls')),
]

# This is a crucial addition for serving static files correctly.
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)