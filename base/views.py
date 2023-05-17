from django.shortcuts import render, HttpResponse
from .models import Startup
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StartupSerializer, StartupFormSerializer
from .forms import StartupForm

@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        startup = Startup.objects.all()
        serializer = StartupSerializer(startup, many=True,context = {startup:startup})
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = StartupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

   


# class StartupFormView(APIView):
#     def post(self, request):
#         serializer = StartupFormSerializer(data=request.data)
#         if serializer.is_valid():
#             # Perform actions based on the form data
#             name_value = serializer.validated_data['name']
#             members_value = serializer.validated_data['members']
#             found_value = serializer.validated_data['found']
#             #pitch_file = serializer.validated_data['pitch']
#             # ...
#             return Response({'success': True})
#         else:
#             return Response(serializer.errors, status=400)
