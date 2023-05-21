from .models import Startup, Contact
from rest_framework import serializers 


class StartupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startup
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class StartupSubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startup
        fields = '__all__'