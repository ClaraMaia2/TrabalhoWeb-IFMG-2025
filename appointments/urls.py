from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('new/', views.create_appointment, name='create'),
    path('my/', views.my_appointments, name='my_appointments'),
    path('all/', views.all_appointments, name='all_appointments'),
]
