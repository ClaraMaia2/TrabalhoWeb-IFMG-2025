from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from datetime import datetime
from .models import Appointment, Service
from .utils import AVAILABLE_TIMES

@login_required
def create_appointment(request):
    services = Service.objects.all()
    available_times = AVAILABLE_TIMES
    
    if request.method == 'POST':
        date_appointment = request.POST['date_appointment']
        time_appointment = request.POST['time_appointment']
        service_id = request.POST['service']
        
        Appointment.objects.create(
            client=request.user,
            service_id=service_id,
            date_appointment=date_appointment,
            time_appointment=time_appointment
        )
        
        return redirect('my_appointments')
    #enddef
    
    selected_date = request.GET.get('date_appointment')
    
    if selected_date:
        occupied = Appointment.objects.filter(date_appointment=selected_date).values_list('time', flat=True)
        
        occupied = [t.strftime('%H:%M') for t in occupied]
        
        available_times = [h for h in AVAILABLE_TIMES not in occupied]
    #endif
    
    return render(request, 'appointments/make_appointment.html', {'services': services, 'available_times': available_times})
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