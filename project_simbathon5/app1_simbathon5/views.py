from django.shortcuts import render
from .models import Reserv
# Create your views here.

def showmain(request):
    return render(request, 'app1_simbathon5/index.html')