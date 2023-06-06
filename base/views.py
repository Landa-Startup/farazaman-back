from django.shortcuts import HttpResponse
from .models import Startup, Contact, StartupSubmit, Event, Hire
from rest_framework import viewsets
from .serializers import StartupSerializer, ContactSerializer, StartupSubmitSerializer, EventSerializer, HireSerializer
from rest_framework.parsers import FormParser, MultiPartParser
from django.middleware.csrf import get_token
from rest_framework.views import APIView
from rest_framework.response import Response


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
    parser_classes = [FormParser, MultiPartParser]
    http_method_names = ['post']


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    http_method_names = ['get']


class HireViewSet(viewsets.ModelViewSet):
    queryset = Hire.objects.all()
    serializer_class = HireSerializer
    http_method_names = ['post']

# for generate csrf token


class CSRFTokenView(APIView):
    def get(self, request, format=None):
        token = get_token(request)
        return Response({'csrfToken': token})
