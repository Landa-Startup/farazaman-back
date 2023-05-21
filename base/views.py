from django.shortcuts import render, HttpResponse
from .models import Startup, Contact, StartupSubmit
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializers import StartupSerializer, ContactSerializer



def index(request):
    return HttpResponse("index page")

@api_view(['GET'])
def startups(request):
    if request.method == 'GET':
        startup = Startup.objects.all()
        serializer = StartupSerializer(startup, many=True,context = {startup:startup})
        return Response(serializer.data)
    
def startupsDetail(request, pk):
    startup = Startup.objects.get(id=pk)
    serializer = StartupSerializer(startup, many=False)
    return Response(serializer.data, pk = startup.id)

    
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class StartupSubmitViewSet(viewsets.ModelViewSet):
    queryset = StartupSubmit.objects.all()
    serializer_class = StartupSerializer