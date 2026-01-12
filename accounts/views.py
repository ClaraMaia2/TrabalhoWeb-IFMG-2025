from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import ProfileForm, SignupForm

def sign_up(request):
    if request.method == 'POST':
        user_form = SignupForm(request.POST)
        profile_form = ProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            with transaction.atomic():
                user = user_form.save()
                
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                
                login(request, user)
                
                return redirect('core:home')
            #endwith
        #endif
    #endif
    else:
        user_form = SignupForm()
        profile_form = ProfileForm()
    #endelse
    
    return render(request, 'accounts/signup.html', {'user_form': user_form, 'profile_form': profile_form,})
#enddef

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')
#enddef
