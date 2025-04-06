from django.urls import path
from .views import *

urlpatterns = [
    path("code_barre/<int:pk>/", code_barre, name="code_barre"),
    # path('retour/', paiement_retour, name='paiement_retour'),
    # path('notification/',   paiement_notification, name='paiement_notification'),

]
