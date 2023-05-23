from .models import Startup, Event
from rest_framework import serializers 


class StartupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startup
        fields = ('id', 'name', 'members', 'fund', 'description', 'logo')

class ContactSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField(required=True)
    message = serializers.CharField()

class StartupSubmitSerializer(serializers.Serializer):
    name = serializers.CharField()
    members_count = serializers.IntegerField()
    email = serializers.EmailField()
    phone = serializers.CharField(required=True)
    pitch = serializers.FileField(required=True)

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'