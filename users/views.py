from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm 
from .forms import UpdateProfileForm, UpdateUserForm
from .models import Profile
from subscriptions.views import check_plan
from subscriptions.models import Subscription

# Create your views here.

@login_required()
def profile(request):
    user = request.user
    profile = Profile.objects.get(user=user) 

    try:
        Subscription.objects.get(user=user) 
    except: 
        return redirect('subscriptions:plans') 


    if request.POST: # Save
            user_form = UpdateUserForm(request.POST, instance=request.user)
            profile_form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
            if user_form.is_valid() and profile_form.is_valid():
                # user_update.save(commit=False)
                user_form.save()

                profile_form.save(commit=False) 
                profile_form.user = request.user 
                profile_form.save()
                print('Saved !!!')
                print('save successfully !') # test code 
    else: # Show
        user_form = UpdateUserForm(instance=user)
        profile_form = UpdateProfileForm(instance=profile)

    context = {
        'user_form': user_form, 
        'profile_form': profile_form
    } 
    return render(request, 'users/profile.html', context)
