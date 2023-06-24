from django.shortcuts import render
from .models import * 

# Create your views here.

def list_frameworks(request):
    systems = System.objects.all()

    context = {
        'systems': systems
    }

    return render(request, 'system/frameworks.html', context)


def framework_details(request, slug): 
    system = System.objects.get(slug=slug) 

    context ={
        'system': system
    }

    return render(request, 'system/framework-details.html', context)