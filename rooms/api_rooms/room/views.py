from rest_framework.decorators import action
from rest_framework import viewsets


from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from room.models import Client

from room.serializers import ClientSerializer


# Quando uma viewSet recebe uma request existem dois atributos obrigatorios
# que devem ser levados em consideracao:
# 1-queryset: Dita quais dados do db podem e devem ser acessados
# pelo ViewSet e suas actions

# 2-o serialziaer formata os dados do db para que possamos recebe-los
# no backend já formatados para usa-los

# quando uma action é recebida a primeira coisa que é
# procurada dentro da classe sao os metodos get referentes ao
# queryset e ao serializer_class esses metodos vao definir qual
# objetos serializer_class e queryset que deverao ser retornados
# baseados nos metodos de request recebidos


class LoginViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


    # def get_queryset(self):
    #     pass

    # def get_serializer_class(self):
    #     if self.action in ['CREATE', 'UPDATE']:
    #         return CreateClientSerializer




    @action(methods=['POST'], detail=False)
    def confirm(self, request):
        print(request.data)
        breakpoint()
        db_user = Client.objects.filter(name=request.data['name'], passw=request.data['passw'])
        if len(db_user):
             return response.Response(status=200, data="Logou!")
        return  response.Response(status=404)




# Create your views here.

def home(request):
    return HttpResponse("pato", status=202)
