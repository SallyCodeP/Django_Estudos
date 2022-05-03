from django.contrib import admin
from django.urls import path, include


# (15)- iremos invocar as relações do urlpatterns do nosso 
# app dentro do urlpatterns do projeto, e para fazer isso
# iremos executar a função path que nesse caso recebera como parametro 
# o caminho do diretorio de onde achar o urlpatterns do nosso app 

# (16)- para especificar qual é o arquivo ".py" onde urlpatterns do nosso app se encontra
# precisamos da função "django.urls.include()" que como parametro recebe o nome
# do arquivo que contem o urlpatterns do nosso app

# (lição 17 no "manage.py")

urlpatterns = [
    path("polls/", include("polls.urls")),
    path('admin/', admin.site.urls),
]
