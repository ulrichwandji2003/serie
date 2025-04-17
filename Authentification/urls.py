from django.urls import path
from .views import *

urlpatterns = [
    path('inscription', Inscription, name="inscription"),
    path('inscription1', Inscription1, name="inscription1"),
    path('connexion', Connexion, name="connexion"),
    path('avis/', avis, name='avis'),
    path('propo', Propo, name="propo"),
    path('contact', contact, name="contact"),
    path('acc', navebare2, name="navebare2"),

]