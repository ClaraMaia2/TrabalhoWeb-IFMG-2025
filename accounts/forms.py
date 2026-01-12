from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    #endclass
    
    def save(self, commit=True):
        user = super().save(commit=False)
        
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
        #endif
        
        return user
    #enddef
#endclass

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        
        fields = ('cpf', 'sexo', 'data_nascimento', 'celular')
        
        widgets = {'data_nascimento': forms.DateInput(attrs={'type': 'date'})}
    #endclass
#endclass