"""helloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
