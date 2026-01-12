from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    name = models.TextField(max_length=100)
    
    def __str__(self):
        return self.name
    #enddef
#endclass

class Appointment(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='appointments')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    
    client_name = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    date_appointment = models.DateField()
    time_appointment = models.TimeField()
    
    # Configura o comportamento do model, ou seja, define regras e opções do model
    class Meta:
        # Impedindo dois agendamentos no mesmo dia e horário
        unique_together = ('date_appointment', 'time_appointment')
        ordering = ['date_appointment', 'time_appointment'] # Define a ordem padrão dos resultados quando buscar agendamentos
    #endclass
    
    def __str__(self):
        return f'{self.service}: {self.date_appointment} - {self.time_appointment}'
    #enddef
#endclass
