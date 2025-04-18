from django.shortcuts import *
from .models import *

# Create your views here.

def detail_stream(request,pk):
    
    detail_stream= Streaming.objects.get(pk=pk)
    context = { 
        "detail_stream":detail_stream 
    }
    return render(request, "Streaming/detail_stream.html",context)


def film(request):

    stream = Streaming.objects.filter(Type_streaming = "film")
    context = {
        "stream": stream
    }
    

    return render(request, "choix/Film.html",context)


def serie(request):

    stream = Streaming.objects.filter(Type_streaming = "serie")
    context = {
        "stream": stream
    }
    

    return render(request, "choix/Serie.html",context)

def anime(request):

    stream = Streaming.objects.filter(Type_streaming = "anime")
    context = {
        "stream": stream
    }
    

    return render(request, "choix/Anime.html",context)

def comedie(request):

    stream = Streaming.objects.filter(Type_streaming = "comedie")
    context = {
        "stream": stream
    }
    

    return render(request, "choix/Comedie.html",context)
