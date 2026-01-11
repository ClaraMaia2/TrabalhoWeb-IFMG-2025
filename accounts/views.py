from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Profile

def sign_up(request):
    if request.method == 'POST':
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'], email=request.POST['email'])
        
        Profile.objects.create(
            user=user, 
            cpf=request.POST['cpf'], 
            sexo=request.POST['sexo'], 
            data_nascimento=request.POST['data_nascimento'], 
            celular=request.POST['celular']
        )
        
        login(request, user)
        
        return redirect('home')
    #endif
    
    return render(request, 'accounts/signup.html')
#enddef

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')
#enddef
