from django.shortcuts import *
from Streaming.models import *
from django.http import JsonResponse
import cinetpay
import os
import requests
import uuid
# from cinetpay._client import Client
# from cinetpay import CinetPayClient
# from cinetpay._client import CinetPayClient
# from cinetpay._utils import generate_transaction_id


# Create your views here.

from django.conf import settings

SITE_ID = settings.CINETPAY_SITE_ID
API_KEY = settings.CINETPAY_API_KEY

# SITE_ID = os.environ.get('105890778')
# API_KEY = os.environ.get('143797943467e42d9ddb5c88.31998236')
API_URL = "https://api-checkout.cinetpay.com/v2/payment"
def code_barre(request,pk):
        


    if not SITE_ID or not API_KEY:
        return JsonResponse({"error": "Clés API non configurées"}, status=500)

    if request.method == 'POST':
        montant = ('1000')
        
        if not montant:
            return JsonResponse({"error": "Le montant est requis"}, status=400)

        transaction_id = str(uuid.uuid4())  # Générer un ID unique
        
        data = {
            "apikey": API_KEY,
            "site_id": SITE_ID,
            "amount": 1000,
            "description": "Achat de produit",
            "currency": "XOF",
            "transaction_id": transaction_id,
            "customer_name": "Nom Client",
            "customer_surname": "Prénom Client",
            "customer_email": "email@example.com",
            "customer_phone_number": "674535824",
            "notify_url": "http://127.0.0.1:8000/notify/",
            "return_url": "https://127.0.0.1:8000/success/",
        }

        try:
            response = requests.post(API_URL, json=data)
            response.raise_for_status()  # Vérifie si la requête a échoué

            response_data = response.json()

            if response_data.get('code') == "201" and response_data.get('data'):
                payment_url = response_data['data'].get('payment_url')
                if payment_url:
                    return redirect(payment_url)
                else:
                    return render(request, 'paiements/echec_paiement.html', {'erreur': "URL de paiement introuvable"})
            else:
                return render(request, 'paiements/echec_paiement.html', {'erreur': response_data})

        except requests.exceptions.RequestException as e:
            return render(request, 'paiements/echec_paiement.html', {'erreur': str(e)})

    # Récupération des infos du modèle Streaming
    try:
        info = Streaming.objects.get(pk=pk)
    except Streaming.DoesNotExist:
        return JsonResponse({"error": "Contenu introuvable"}, status=404)
        








    info = Streaming.objects.get(pk=pk)

    context = {
            "info" : info
    }

    return render(request, "Streaming/code_barre.html",context)




# def paiement_retour(request):
#         # Gérer le retour après le paiement
#     return render(request, 'paiements/paiement_retour.html')

# def paiement_notification(request):
#         # Gérer les notifications de paiement (webhook)
#         # ... validation de la transaction ...
#     return HttpResponse(status=200)