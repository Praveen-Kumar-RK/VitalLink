from django.shortcuts import render
from django.http import HttpResponse
from .models import one
# Create your views here.

def index(response):
    return render(response,"main/index.html", {})

def choose(request):
    return render(request,'main/choose-login/block.html', {})

def login(request):
    return render(request,'main/login/login.html', {})

def signup(request):
    return render(request,'main/login/signup.html', {})

def PatientReg(request):
    return render(request,'main/registeration/patient.html', {})

def PatientReg2(request):
    return render(request,'main/registeration/pnext.html', {})

def DoctorReg(request):
    return render(request,'main/registeration/doctor-registeration.html', {})