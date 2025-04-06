from django.shortcuts import render
from Streaming.models import *

def reservation(request,pk):

    reservation = Streaming.objects.get(pk=pk)

    context = {
                "reservation" : reservation,
        }

    return render(request, "Streaming/Reservation.html",context)

# Vous pouvez aussi créer une fonction pour traiter les réservations si nécessaire
def reservation_salle(request):
    
    return render(request, "Streaming/reservation_salle.html")


