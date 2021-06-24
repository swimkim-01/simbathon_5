from django.urls import path
from .views import *

app_name = "app1_simbathon5"
urlpatterns = [
    path('', home, name= "home"),
    path('calendar/', showmain, name= "showmain"),
    path('reserv/', reservation, name= "reservation")
]