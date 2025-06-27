from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from .models import Clinic, Distributor
from .forms import signupForm, loginForm

def home(request):
    return render(request, 'home.html')

def clinic_signup_home(request):
    return render(request, 'home.html')

def clinic_signin(request):
    clinic_license = request.POST.get('clinic_license')
    password = request.POST.get('password')
    user=authenticate(request, username=clinic_license, password=password)
    if user is not None:
        auth_login(request, user)
        request.session['clinic_license'] = clinic_license
        return redirect('clinic_portal')
    elif request.method == 'POST':
        messages.error(request, 'Invalid license or password')
    else:
        form = loginForm()
    return render(request, 'clinic_in.html', {'form': form})

def clinic_signup(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            license_number = form.cleaned_data.get('license_number')
            password = form.cleaned_data.get('password')
            
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
        else:
            messages.error(request, 'Invalid form submission')
    else:
        form = signupForm()
    return render(request, 'clinic_up.html', {'form': form})

def distributor_signup(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('distributor_signin')  # Redirect to sign-in
    else:
        form = signupForm()
    return render(request, 'distributor_up.html', {'form': form})

def distributor_signin(request):
    # Your existing sign-in view with medical theme
    return render(request, 'distributor_in.html')            


def clinicPortal(request):
    if 'clinic_license' not in request.session:
        return redirect('clinic_signin')
    return render(request, 'clinic.html')

def distributorPortal(request):
    if 'distributor_license' not in request.session:
        return redirect('distributor_signin')
    return render(request, 'distributor.html')

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
    
    return render(request, 'signup.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Clinic, Distributor
from .forms import signupForm, loginForm


def clinic_portal(request):
    if 'clinic_license' not in request.session:
        return redirect('clinic_signin')
    return render(request, 'clinic.html')

def distributor_portal(request):
    if 'distributor_license' not in request.session:
        return redirect('distributor_signin')
    return render(request, 'distributor.html')



