from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import path
from . import views
from django.urls import include, path
from  .models import Product, Supplier, Order

#create views
def home(request):
    return render(request, "home.html")
def signIn(request):
    return render(request, "index.html")
def SignUp(request):
    return render(request, "signUp.Html")


from .forms import ClinicSignUpForm, DistributorSignUpForm
def signUp(request):
    if request.method == 'POST':
        form =ClinicSignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user) # type: ignore
            return redirect('supply-home')
        elif request.method == 'POST':
            form = DistributorSignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('supply-home')
        else:
            return HttpResponse("Invalid form submission")
from django.contrib.auth import login   


# Create your views here.
