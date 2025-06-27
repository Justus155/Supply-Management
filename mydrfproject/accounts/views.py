from django.shortcuts import render
from django.contrib.auth import authenticate
from .serializers import ClinicSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import clinic
# Create your views here.

def home(request):
    return render(request, 'home.html')
@api_view(['POST'])
def clinic_signup(request):
    if request.method == 'POST':
        serializer = ClinicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#clinic login
@api_view(['POST'])
def clinic_login(request):
    if request.method == 'POST':
        license_number = request.data.get('license_number')
        password = request.data.get('password')
        user = authenticate(username=license_number, password=password)
        if user.is_authenticated:
            return render(request, 'clinic.html', {'user': user})

        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)    

#implementing clinic logout
@api_view(['POST'])
def clinic_logout(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
    return Response({"error": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)            

