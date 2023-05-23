from django.shortcuts import HttpResponse
from .models import Startup, Contact, StartupSubmit, Event
from rest_framework import viewsets
from .serializers import StartupSerializer, ContactSerializer, StartupSubmitSerializer, EventSerializer

def index(request):
    return HttpResponse("index page")

class StartupViewSet(viewsets.ModelViewSet):
    queryset = Startup.objects.all()
    serializer_class = StartupSerializer
    http_method_names = ['get']

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    http_method_names = ['post']

class StartupSubmitViewSet(viewsets.ModelViewSet):
    queryset = StartupSubmit.objects.all()
    serializer_class = StartupSubmitSerializer
    http_method_names = ['post']

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    http_method_names = ['get']
    