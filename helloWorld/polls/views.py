
# (6)-O django.shortcuts.render() é uma func que
# serve para renderizar as informações de um html 
from django.shortcuts import render

# (7)-django.http.HttpResponse() é uma func que nos permite  
# definir a resposta que será retornada para o cliente
# após algum link do nosso site ser acessado
from django.http import HttpResponse 

# (8)-Cada configuração de acesso e retorno é feito atravez de uma função def
# chamaremos essas funções de definição de acesso e retorno de request functions

# (9)- Para relacionar uma request function a um link, precisamo configurar uma ligação
# fazemos isso no "urls.py"


def init(request):
    return HttpResponse("Hello World!") 