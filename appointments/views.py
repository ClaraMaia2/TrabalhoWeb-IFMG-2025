from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Appointment, Service
from .forms import FormAppointment
from .utils import AVAILABLE_TIMES

@login_required
def create_appointment(request):
    services = Service.objects.all()
    
    if request.method == 'POST':
        form = FormAppointment(request.POST, user=request.user)
        
        if form.is_valid():
            appointment = form.save(commit=False)
            
            if not request.user.is_staff:
                appointment.client = request.user
                appointment.client_name = ''
            #endifnot
            else:
                appointment.client = None
            #endelse
            
            appointment.save()
            
            return redirect('appointments:my_appointments')
        #endif
    #endif
    else:
        form = FormAppointment(user=request.user)
    #enelse
    
    # ===== GET (filtrar horários disponíveis) ===== 
    selected_date = request.GET.get('date_appointment')
    available_times = AVAILABLE_TIMES
    
    if selected_date:
        occupied = Appointment.objects.filter(date_appointment=selected_date).values_list('time_appointment', flat=True)
        occupied = [t.strftime('%H:%M') for t in occupied]
        available_times = [h for h in AVAILABLE_TIMES if h not in occupied]
    #endif
    
    return render(request, 'appointments/make_appointment.html', {'form': form, 'available_times': available_times, 'services': services})
#enddef

@login_required
def my_appointments(request):
    appointments = Appointment.objects.filter(client=request.user)
    
    return render(request, 'appointments/my_appointments.html', {'appointments': appointments})
#enddef

@staff_member_required
def all_appointments(request):
    appointments = Appointment.objects.all()
    
    return render(request, 'appointments/all_appoinments.html', {'appointments': appointments})
#enddef