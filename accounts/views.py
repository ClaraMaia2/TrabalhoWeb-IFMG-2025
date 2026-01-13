from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
                
                if profile.is_terapeuta:
                    user.is_staff = True
                    user.save(update_fields=['is_staff'])
                #endif
                
                messages.success(request, 'Conta criada com sucesso!')
                
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
def logout_view(request):
    logout(request)
    
    messages.success(request, 'Você saiu da sua conta com sucesso!')
    
    return redirect('core:home')    
#enddef