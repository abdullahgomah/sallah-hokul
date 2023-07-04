from django.urls import path 
from .views import * 

app_name ='subscriptions' 

urlpatterns = [
    path('pricing/', plans, name='plans'),
    path('pricing/<str:plan>/', plan_details, name='plan-details'), 
]