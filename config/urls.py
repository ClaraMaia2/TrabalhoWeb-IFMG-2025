from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # usa o include para delegar parte das URLs para outro arquivo 
    path('', include('core.urls')), # URLs que começam com /core/
    path('accounts/', include('accounts.urls')), # URLs que começam com /accounts/
    path('appointments/', include('appointments.urls')), # URLs que começam com /appointments/
]
