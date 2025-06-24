from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import path
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Product, Supplier, Order
from .forms import ClinicSignInForm, ClinicSignUpForm, DistributorSignInForm, DistributorSignUpForm
from . import views
from django.urls import include, path
from  .models import Product, Supplier, Order
from django.contrib.auth import authenticate
from  .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import generics


def home(request):
    return render(request, "home.html")
def signIn(request):
    return render(request, "index.html")
def SignUp(request):
    return render(request, "signUp.Html")
def clinicsignIn(request):
    if request.method == 'POST':
        clinic_license = request.POST.get('clinic_license')
        password = request.POST.get('password')
        
        
        user = authenticate(request, clinic_license=clinic_license, password=password)
        
        if user.objects.filter(clinic_license=clinic_license, password=password).exists():
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('/clinicWelcome')  # Redirect to home page
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('signIn/')  # Redirect back to login page
    
    return render(request, 'login.html')

@login_required
def clinic_welcome(request):
    if not request.user.is_clinic:  # You'll need to add this check in your user model
        return redirect('home')
    user = request.user
    sdata = ClinicSerializer(user).data
    return render(request, "clinic.html", sdata)

@login_required
def distributor_welcome(request):
    if not request.user.is_distributor:  # You'll need to add this check in your user model
        return redirect('home')
    return render(request, "distributor.html")

# Authentication views
def clinic_sign_in(request):
    if request.method == 'POST':
        form = ClinicSignUpForm(request, data=request.POST)
        if form.is_valid():
            clinic_license = form.cleaned_data.get('clinic_license')
            password = form.cleaned_data.get('password')
            user = authenticate(request, clinic_license=clinic_license, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('clinic_welcome')
        messages.error(request, 'Invalid clinic license or password')
    else:
        form = ClinicSignInForm()
    return render(request, 'clinic_sign_in.html', {'form': form})

def distributor_sign_in(request):
    if request.method == 'POST':
        form = DistributorSignInForm(request, data=request.POST)
        if form.is_valid():
            distributor_license = form.cleaned_data.get('distributor_license')
            password = form.cleaned_data.get('password')
            user = authenticate(request, distributor_license=distributor_license, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('distributor_welcome')
        messages.error(request, 'Invalid distributor license or password')
    else:
        form = DistributorSignInForm()
    return render(request, 'distributor_sign_in.html', {'form': form})

def clinic_sign_up(request):
    if request.method == 'POST':
        form = ClinicSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('clinic_welcome')
    else:
        form = ClinicSignUpForm()
    return render(request, 'clinic_sign_up.html', {'form': form})

def distributor_sign_up(request):
    if request.method == 'POST':
        form = DistributorSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('distributor_welcome')
    else:
        form = DistributorSignUpForm()
    return render(request, 'distributor_sign_up.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

# Product/Order views
@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

@login_required
def create_order(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        # Add order creation logic here
        messages.success(request, 'Order created successfully!')
        return redirect('product_list')
    return render(request, 'create_order.html', {'product': product})




#CLINIC SIGN UP
class clinicSignUpview(generics.CreateAPIView):
    queryset=Clinic.objects.all()
    serializers_class = clinicSignUpSerializer
    permissions_classes = [permissions.AllowAny]
#CLINIC SIGNIN 

class clinicSignInview(generics.CreateAPIView):
    permissions_classes = [permissions.AllowAny]    
class clinicSignUpViewSet(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = clinicSignUpSerializer
    permission_classes = [permissions.IsAuthenticated]
class ClinicSerializerView(APIView):
    def post(self, request):
        clinic_license = request.data.get('clinic_license')
        password = request.data.get('password')
        clinic= authenticate(request, clinic_license=clinic_license, password=password)
        if clinic:
            login(request, clinic)
            return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
