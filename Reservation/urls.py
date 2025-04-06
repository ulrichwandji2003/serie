from django.urls import path
from .views import *

urlpatterns = [
    path("reservation/<int:pk>/", reservation, name="reservation"),
    path("reservation_salle/", reservation_salle, name="reservation_salle"),


]

