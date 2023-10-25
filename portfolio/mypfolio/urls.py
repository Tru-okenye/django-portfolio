from django.urls import path
from . import views


app_name ="mypfolio"
urlpatterns = [
    path('', views.index, name="index"),
    
]