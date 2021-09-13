from django.contrib import admin

from .models import Client, Company



@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name','cpf','document']
    
    def get_queryset(self, request):
        user = request.user
        client = Client.objects.get(name = user)
        if client.type == 'Admin':
            return super().get_queryset(request).all()
        return super().get_queryset(request).filter(name = request.user) 
    

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name','address','city','status','email']
