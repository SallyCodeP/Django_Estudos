from django_rest import viewsets
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from room.models import User

class login(viewsets.ModelViewSet):


    @action(methods=['POST'], detail=False)
    def confirm(self, *args, **kwargs):
        db_user = User.objects.filter(name=kwargs['name'])
        db_passw = User.objects.filter(passw=kwargs['passw'])

        if len(db_user) and len(db_passw):
            return response.Response(status=200, data="Logou!")


        breakpoint()
# Create your views here.

def home(request):
    return HttpResponse("pato", status=202)
