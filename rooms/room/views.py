from rest_framework.decorators import action
from rest_framework import viewsets


from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from room.models import Client

from room.serializers import ClientSerializer

class LoginViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


    



    # @action(methods=['POST'], detail=False)
    # def confirm(self, *args, **kwargs):
    #     db_user = Client.objects.filter(name=kwargs['name'])
    #     db_passw = Client.objects.filter(passw=kwargs['passw'])
    #     breakpoint()
    #     if len(db_user) and len(db_passw):
    #         return response.Response(status=200, data="Logou!")




# Create your views here.

def home(request):
    return HttpResponse("pato", status=202)
