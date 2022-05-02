# Generated by Django 4.0.4 on 2022-05-02 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('psw', models.CharField(db_index=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='connect_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('photo', models.ImageField(upload_to='')),
                ('online', models.BooleanField()),
                ('in_call', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='room.client')),
            ],
        ),
    ]
