from django.contrib import admin
from room.models import Client
from django.contrib import admin

# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    search_fields = ['name']

