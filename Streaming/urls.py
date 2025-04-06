from django.urls import path
from .views import *

urlpatterns = [
    path("detail_stream/<int:pk>/", detail_stream, name="detail_stream"),
    path("cine.nice/film", film, name="film"),
    path("cine.nice/anime", anime, name="anime"),
    path("cine.nice/serie", serie, name="serie"),
    path("cine.nice/comedie", comedie, name="comedie"),

]