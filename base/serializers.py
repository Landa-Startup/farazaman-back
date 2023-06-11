from .models import Startup, Event, Contact, StartupSubmit, Hire, EventAttendees
from rest_framework import serializers


class StartupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startup
        fields = ('id', 'name', 'members', 'fund', 'description', 'logo')


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'message', 'phone', 'created_at']
        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        validated_data['phone'] = self.initial_data.get('phone')

        if not validated_data['phone']:
            raise serializers.ValidationError("Phone is required.")

        return super().create(validated_data)


class StartupSubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartupSubmit
        fields = ['id', 'name', 'members_count', 'email', 'phone', 'pitch']
        read_only_fields = ['id']

    def create(self, validated_data):
        validated_data['phone'] = self.initial_data.get('phone')
        validated_data['pitch'] = self.initial_data.get('pitch')

        if not validated_data['phone']:
            raise serializers.ValidationError("Phone is required.")

        if not validated_data['pitch']:
            raise serializers.ValidationError("Pitch is required.")

        return super().create(validated_data)


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class HireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hire
        fields = '__all__'


class EventAttendeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventAttendees
        fields = '__all__'
        