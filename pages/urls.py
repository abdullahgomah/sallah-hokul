from django.urls import path 
from .views import * 

app_name = 'pages' 

urlpatterns = [
    path("", index, name='index'),
    path('pricing/', plans, name='plans'), 
]
