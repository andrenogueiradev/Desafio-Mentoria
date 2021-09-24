from rest_framework import viewsets
import rest_framework
from rest_framework import authentication
from rest_framework import permissions
from .models import Client, Company
from .serializer import ClientSerializer, CompanySerializer

from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def  get(self, request, format = None):
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
        }
        return Response(content)

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer 
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def  get(self, request, format = None):
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
        }
        return Response(content)

    


