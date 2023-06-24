from django.urls import path 
from .views import * 

app_name = 'system' 

urlpatterns = [
    path('system/<slug:slug>', framework_details, name='framework-details'), 

    path('all', list_frameworks, name='list-frameworks'), 
]