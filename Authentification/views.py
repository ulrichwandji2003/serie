from inspect import ismethod
from django.shortcuts import *
from Streaming.models import Streaming,Contact
from Reservation.models import Avis

# Create your views here.


def Inscription(request):
    return render(request, "Inscription/inscription.html")

def Connexion(request):
    return render(request, "Connexion/Connexion.html")

def avis(request):

    if request.method == 'POST':
        # Récupérer les données du formulaire
        nom = request.POST.get('nom')
        commentaire = request.POST.get('commentaire')
        note = request.POST.get('note')

        # Créer un nouvel avis
        Avis.objects.create(nom=nom, commentaire=commentaire, note=note)

        # Rediriger vers la même page après soumission
        return redirect('avis')

    # Récupérer tous les avis pour les afficher
    avis_list = Avis.objects.all().order_by('-date')
    return render(request, 'accueil/avis.html', {'avis_list': avis_list})
    

def Propo(request):
    return render(request, "accueil/propo.html")

def contact(request):

    if request.method == "POST":

        data = request.POST

        nom = data["nom"]
        email = data["email"]
        message = data["message"]

        contact = Contact(Nom=nom, Email=email,Message=message)
        # print(nom, email, message)
        contact.save

    return render(request, "accueil/contacte.html")

def navebare2(request):

    stream = Streaming.objects.all()
    context = {
        "stream": stream
    }

    return render(request, "navebare2.html",context)