from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Startup, Event, Contact, StartupSubmit, Hire, EventAttendees, WorkSpace


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
            raise ValidationError({"phone": "Phone is required."})

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
            raise ValidationError({"phone": "Phone is required."})

        if not validated_data['pitch']:
            raise ValidationError({"pitch": "Pitch is required."})

        return super().create(validated_data)


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'date', 'time', 'location', 'link', 'created_at', 'updated_at', 'flag', 'image')


class HireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hire
        fields = ('id', 'name', 'phone', 'hireType', 'resume')
        read_only_fields = ['id']


class EventAttendeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventAttendees
        fields = ('id', 'name', 'email', 'phone', 'event', 'created_at')
        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        validated_data['phone'] = self.initial_data.get('phone')

        if not validated_data['phone']:
            raise ValidationError({"phone": "Phone is required."})

        return super().create(validated_data)


class WorkSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSpace
        fields = ('id', 'name', 'email', 'phone', 'created_at')
        read_only_fields = ['id', 'created_at']
