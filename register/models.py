from os import name
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from .validators import validate_CNPJ, validate_CPF, valida_cnpj
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


def upload_file_customer(instance, filename):
    return f'{instance.name}-{filename}'

class Client(models.Model):
    name = models.CharField(max_length=255)#, verbose_name = 'Nome')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cpf = models.CharField('CPF',unique=True, max_length=14, validators=[validate_CPF], blank=True, null=True)#, verbose_name = 'CPF')
    email = models.EmailField(max_length=50, blank=True, null=True)
    document = models.FileField(upload_to= 'meusarquivos', blank=False, null=True)
    type = models.CharField(max_length=255, verbose_name = ('Tipo de Usuário'), blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} - {self.cpf}'


class Company(models.Model):
    managers = models.ManyToManyField(User, related_name='company', blank = True) #verbose_name='Gerente' )
    name = models.CharField(max_length=30) #verbose_name= 'Nome'#)
    cnpj = models.CharField('CNPJ', max_length=18, validators=[validate_CNPJ, valida_cnpj], blank=True, null=True)
    email = models.EmailField(max_length=50)
    status = models.CharField(max_length=30)
    address = models.CharField(max_length=90) #verbose_name='Endereço')
    city = models.CharField(max_length=30)# verbose_name='Cidade')

    class Meta:
        verbose_name_plural = 'Company'

    def __str__(self):
        return self.name    

       
        
