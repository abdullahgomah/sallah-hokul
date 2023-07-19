from django.shortcuts import render
from system.models import System
from .models import Info, Home 




# Create your views here.
def index(request): 
    systems = System.objects.all() 
    main_info = Home.objects.last() 

    context = {
        'systems': systems,
        'main_info': main_info 
    } 
    return render(request, 'pages/index.html', context)



def about(request): 
    info = Info.objects.last() 
    context = {
        'info': info 
    }
    return render(request, 'pages/about.html', context)