from rest_framework import serializers
from pachecoApp.models import Automovil

class AutomovilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Automovil
        fields = '__all__'