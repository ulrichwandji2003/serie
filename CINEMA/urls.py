from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from CINEMA import settings
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', navebare1, name="navebare1"),
    path('', include('Authentification.urls')),
    path('', include('Streaming.urls')),
    path('', include('Reservation.urls')),
    path('', include('Code_barre.urls')),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
