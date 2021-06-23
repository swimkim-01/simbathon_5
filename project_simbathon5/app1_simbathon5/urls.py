from django.urls import path
from .views import *

app_name = "app1_simbathon5"
urlpatterns = [
    path('', showmain, name= "showmain"),
]