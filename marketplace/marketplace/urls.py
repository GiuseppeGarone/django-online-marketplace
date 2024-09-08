# workaround to display images in development env
# (remove when in production env!)
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path

from core.views import index, contact

# don't add static resources like this in production!
urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
