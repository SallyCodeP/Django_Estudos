#!/usr/bin/env python
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'helloWorld.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # (1)-Para criar um projeto dentro do django usamos o comando inicial 
    # "django-admin startproject (nome do site)"

    # (2)-Para iniciar o servidorweb usamos o comando
    # "python3 manage.py runserver"

    # (3)-O django interpreta todos os mecanismos de um projeto como um app
    # ou seja dentro de um projeto django existem diversos apps que podem ou não
    # se comunicar entre sí e que são contruidos independentemente 

    # (4)-apps são criados apartir de uma estrutura base: as pools
    # polls são modulos pre definidos que são padrões dentro de um app
    # para importar o modelo poll usamos comando:
    # python3 manage.py startapp polls

    # (5)-O workflow do django funciona atravez da estrutura mtv ou:
    # model template view, essa estrutura basicamente define os diferentes
    # links do site que estamos criando e oque deve ser retornado
    # para cada um desses links e definimos isso no "views.py"

    # (17)-Agora iremos conferir se todas as dependencias do gerenciador de db
    # do nosso app estão instaladas e funcionando, para isso iremos usar o comando
    # "python3 manage.py migrate"
    # lição 18 está no "models.py"
    main()
