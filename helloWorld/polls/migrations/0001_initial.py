# Generated by Django 4.0.4 on 2022-04-25 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perguntas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta', models.CharField(default='', max_length=200)),
                ('data', models.DateTimeField(default=0)),
            ],
        ),
    ]
