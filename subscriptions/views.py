from django.shortcuts import render, redirect
from .models import * 
from django.contrib.auth.decorators import login_required
import datetime 


def check_plan(user):
    from subscriptions.models import Subscription
    user = user 
    try: 
        Subscription.objects.get(user=user) 
    except: 
        return redirect("subscriptions:plans")

# Create your views here.
def plans(request):
    plans = Plan.objects.all()
    context = {
        'plans': plans 
    } 
    return render(request, 'subscriptions/plans.html', context)


@login_required
def plan_details(request, plan):
    
    plan = Plan.objects.get(name=plan) 
    paypal = PayPal.objects.last() 

    print(paypal) 

    context = {
        'plan': plan, 
        'paypal': paypal
    } 
    return render(request, 'subscriptions/plan-details.html', context)


@login_required
def create_subscription(request): 
    user = request.user 

    try: 
        Subscription.objects.get(user=user) 
        return render(request, 'subscriptions/already-subscribed.html')
    except: 
        pass 

    start_date = datetime.datetime.now().date() 

    plan = request.POST['plan'] 
    # start_date = request.POST['start_date'] 

    selected_plan = Plan.objects.get(name=plan) 

    new_subscription = Subscription.objects.create(user=user, plan=selected_plan, start_date=start_date)


    context = {} 
    return render(request, 'subscriptions/congratulations.html', context)


    