from operator import contains
from django.db import models
from django.utils import timezone

# Create your models here.

# (18) - Models são estruturas nas quais definimos 
# o comportamento/funcionamento de alguma classe de dados
# do banco de dados

# (19) - precisamos ativar o models do nosso app, e para isso 
# iremos no settings.py do nosso projeto
# Lição 20 no settings.py

# (21) - Para criar um model, primeiro criamos uma class
# e a colocamos para herdar as propriedades da classe mãe 
# models.Model 

# (22) - Após criar um model, para instala-lo dentro do projeto precisamos executar
# "python3 manage.py makemigrations polls", ao executar esse comando tendo
# colocado no settings.py do projeto que o comportamento do nosso app deve ser instalado
# os models do nosso app serão importados para dentro do projeto 

class Perguntas(models.Model):
    # (23) - Para cada campo informação que um model carrega criamos uma variavel
    # onde dentro dessa variavel definimos que tipos de dados que este campo pode receber

    # (24) - Usamos models types para definir os tipos de dados que um campo pode armazenar
    # para invocar models types usamos model functions, 
    # essas funções aleḿ de retornar models types, elas nos permite expecificar regras por exemplo:  
    # Na função "models.CharField()" que retorna o model type Char (permite armazenar strings) 
    # podemos especificar como parametro uma regra que dita 
    # a quantia maxima de caracteres que o model type Char pode armazenar naquele campo 
    pergunta = models.CharField(default="",max_length=200)

    # A model function DateTimeField() retorna o model type DateTime que permite armazenar
    # data e horario
    data = models.DateTimeField(default=0)

    # (25) - Podemos criar metodos para nossos models (funciona exatamente como classes) 
    def mostrar_data_das_perguntas(self):
        return self.pergunta
    
    def __str__(self):
        # (26) - O metodo __str__ define oque será retornado quando 
        # os valores do model perguntas forem chamados
        return self.pergunta


# (27) - Existem diversos metodos que podem manipular os dados existentes dentro de um models,
# para usarmos esses metodos primeiramente colocamos o nome do nosso model, 
# após isso inserimos o nome do atributo que queremos manipular 
# (caso queiramos nos referir a tds os dados usamos o atributo objects) e finalmente acrescentamos
# o metodo que queremos usar
# Temos metodos como:

# nome_do_model.objects.get(atributo="valor_que_queremos_preocurar")
# o metodo get() retorna o objeto model que tiver exatamente os mesmos elementos que os 
# especificados nos parametros de busca  

# nome_do_model.objects.filter(atributo="valor_que_queremos_preocurar")
# funciona exatamente como o metodo get, mas diferente do get, o filter retorna
# TODOS os objetos model que tiverem exatamente os mesmos elementos que os 
# especificados nos parametros de busca  


# (28) - Para podermos testar os metodos dos nossos models e ativar funções do nosso app manualmente
# podemos usar a API de controle do Django usando o comando: "python3 manege.py shell"

# (29) - Para armazenar dados pelos models criamos um objeto com aquile model e depois o salvamos
# Exemplo: 
# teste = Perguntas(pergunta="pato?", data="timezone.now()")
# teste.save()
# Agora se chamarmos "Perguntas.objects.all()" 
# (metodo que retorna todos os dados referentes aquele model no banco de dados)
# iremos ver os dados q criamos no objeto teste

