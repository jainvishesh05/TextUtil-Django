from django.urls import path
from .import views

urlpatterns = [ 
    path('' , views.Home , name = 'home'),
    path('result' , views.result , name ='result'),
    ]