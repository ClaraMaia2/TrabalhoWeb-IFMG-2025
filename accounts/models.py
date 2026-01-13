from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


exactly_11_digits_validator = RegexValidator(
    regex=r'^\d{11}$',
    message='Este campo deve conter exatamente 11 números.'
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    
    celular = models.CharField(
        max_length=11,
        validators=[exactly_11_digits_validator],
    )

    cpf = models.CharField(
        max_length=11,
        unique=True,
        validators=[exactly_11_digits_validator],
    )

    data_nascimento = models.DateField()

    is_terapeuta = models.BooleanField(default=False)

    sexo = models.CharField(max_length=1, choices=[
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ])
    
    def __str__(self):
        return self.user.username
    #enddef
#endclass
