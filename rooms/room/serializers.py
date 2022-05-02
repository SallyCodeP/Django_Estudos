from rest_framework import serializers
from room import models



class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Client
        fields = ['name', 'psw']
        # fields = '__all__'
