from django.shortcuts import render
from .models import Reserv
# Create your views here.

def home(request):
    return render(request, 'app1_simbathon5/main.html')

def showmain(request):
    return render(request, 'app1_simbathon5/index.html')

def reservation(request):
    return render(request, 'app1_simbathon5/reserv.html')