from django import forms
from .models import Appointment

class FormAppointment(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['client_name', 'service', 'date_appointment', 'time_appointment']
    #endclass
    
    def __init__(self, *args, user=None, **kwargs):
        self.user = user
        
        super().__init__(*args, **kwargs)
    #enddef
    
    def clean_form(self):
        cleaned_data = super().clean()
        client_name = cleaned_data.get('client_name')
        
        if self.user.is_staff:
            if not client_name:
                raise forms.ValidationError('Para agendamento feito pelo(a) terapeuta, o nome do cliente é obrigatório')
            #endifnot
        #endif
        else:
            cleaned_data['client_name'] = ''
        #endelse
        
        return cleaned_data
    #enddef
#endclass