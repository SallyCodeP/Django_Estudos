from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, db_index=True)
    psw = models.CharField(max_length=255, db_index=True)


class connect_user(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    ip = models.IPAddressField()
    photo = models.ImageField()
    online = models.BooleanField()
    in_call = models.BooleanField()

class friend(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField()
