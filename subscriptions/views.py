from django.shortcuts import render
from .models import * 

# Create your views here.
def plans(request):
    plans = Plan.objects.all()
    context = {
        'plans': plans 
    } 
    return render(request, 'subscriptions/plans.html', context)

def plan_details(request, plan):
    plan = Plan.objects.get(name=plan) 
    paypal = PayPal.objects.last() 

    print(paypal) 

    context = {
        'plan': plan, 
        'paypal': paypal
    } 
    return render(request, 'subscriptions/plan-details.html', context)