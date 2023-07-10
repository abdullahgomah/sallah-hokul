from django.shortcuts import render
from system.models import System

# Create your views here.
def index(request): 
    systems = System.objects.all() 
    context = {
        'systems': systems 
    } 
    return render(request, 'pages/index.html', context)



def about(request): 
    context = {}
    return render(request, 'pages/about.html', context)