from inspect import ismethod
from django.shortcuts import render
from Streaming.models import Streaming,Contact

# Create your views here.

def Inscription1(request):
    return render(request, "Inscription/Inscription1.html")

def Inscription(request):
    return render(request, "Inscription/Inscription.html")

def Connexion(request):
    return render(request, "Connexion/Connexion.html")

def Avis(request):
    return render(request, "accueil/avis.html")

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