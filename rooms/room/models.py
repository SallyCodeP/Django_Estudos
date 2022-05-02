from posixpath import basename
from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    psw = models.CharField(max_length=255, db_index=True)


class connect_user(models.Model):
    user = models.ForeignKey(Client, on_delete=models.PROTECT, basename='client')
    ip = models.GenericIPAddressField()
    photo = models.ImageField()
    online = models.BooleanField()
    in_call = models.BooleanField()

class friend(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField()
