from django.contrib import admin

from .models import Client, Company


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name','cpf','document']

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name','address','city','status','email']
 