from django.urls import path
from . import views
from mypro import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.create_profile),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
