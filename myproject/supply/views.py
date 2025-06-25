from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Clinic, Distributor

def home(request):
    return render(request, 'home.html')

def clinic_signup(request):
    if request.method == 'POST':
        license_number = request.POST.get('license_number')
        password = request.POST.get('password')
        
        if not license_number.startswith('C'):
            messages.error(request, 'Clinic license must start with C')
            return redirect('clinic_signup')
            
        try:
            clinic = Clinic(license_number=license_number)
            clinic.set_password(password)
            clinic.save()
            messages.success(request, 'Clinic account created successfully!')
            return redirect('clinic_signin')
        except Exception as e:
            messages.error(request, f'Error creating account: {str(e)}')
    
    return render(request, 'SignUp.html')

def distributor_signup(request):
    if request.method == 'POST':
        license_number = request.POST.get('license_number')
        password = request.POST.get('password')
        
        if not license_number.startswith('D'):
            messages.error(request, 'Distributor license must start with D')
            return redirect('distributor_signup')
            
        try:
            distributor = Distributor(license_number=license_number)
            distributor.set_password(password)
            distributor.save()
            messages.success(request, 'Distributor account created successfully!')
            return redirect('distributor_signin')
        except Exception as e:
            messages.error(request, f'Error creating account: {str(e)}')
    
    return render(request, 'SignUp.html')

def clinic_signin(request):
    if request.method == 'POST':
        license_number = request.POST.get('license_number')
        password = request.POST.get('password')
        
        try:
            clinic = Clinic.objects.get(license_number=license_number)
            if clinic.check_password(password):
                request.session['clinic_license'] = license_number
                return redirect('clinic_portal')
            else:
                messages.error(request, 'Invalid password')
        except Clinic.DoesNotExist:
            messages.error(request, 'Clinic not found')
    
    return render(request, 'index.html')

def distributor_signin(request):
    if request.method == 'POST':
        license_number = request.POST.get('license_number')
        password = request.POST.get('password')
        
        try:
            distributor = Distributor.objects.get(license_number=license_number)
            if distributor.check_password(password):
                request.session['distributor_license'] = license_number
                return redirect('distributor_portal')
            else:
                messages.error(request, 'Invalid password')
        except Distributor.DoesNotExist:
            messages.error(request, 'Distributor not found')
    
    return render(request, 'index.html')

def clinic_portal(request):
    if 'clinic_license' not in request.session:
        return redirect('clinic_signin')
    return render(request, 'clinic.html')

def distributor_portal(request):
    if 'distributor_license' not in request.session:
        return redirect('distributor_signin')
    return render(request, 'distributor.html')


