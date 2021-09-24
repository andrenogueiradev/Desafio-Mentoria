from rest_framework import serializers
from register.models import Client, Company


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['name','cpf','email','document']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name','address','city','status','email']        