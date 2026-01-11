from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    
    celular = models.CharField(max_length=15)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    is_terapeuta = models.BooleanField(default=False)
    sexo = models.CharField(max_length=1, choices=[
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ])
    
    def __str__(self):
        return self.user.username
    #enddef
#endclass
