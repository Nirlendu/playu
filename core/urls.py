from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from app.views import index, profile, rankings

urlpatterns = [
    url(r'^$', index),
    url(r'^profile/$', profile),
    url(r'^rankings/$', rankings),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)