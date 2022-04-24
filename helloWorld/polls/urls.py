# (10)-A funçao django.urls.path() nos permite relacionar um link
# a uma requst function
from django.urls import path

# (11)- Para nos referir as nossas request functions precisamos importar o "view.py"
from . import views

# (12)-Guardamos as relações entre a request funtions e os links dentro de uma array
# no nosso caso chamaremos essa array de urlpatterns ("camadas_url") pois 
# é exatamente isso que ela representa 
urlpatterns = [

    # (13)-Para relacionar uma request function a um link usamos a função path
    # a função path() recebe 3 parametros:
    # -Uma string contendo o link que queremos relacioanr
    # -A request function que queremos relacionar com o link
    # -O nome que iremos usar para nos referir à relação 
    path("home/", views.init, name="first")
]

# (14)-Já que estamos contruindo um app dentro de um modelo poll
# nada oque fizemos até agora aqui será executado ao iniciarmos o web server do projeto
# para que tudo oque nos fizemos no urls.py desse app seja implementado no projeto,
# precisamos chamar nossa lista de relações ("urlpatterns") dentro do urls.py do projeto
# (a lição 15 está no urls.py do projeto)