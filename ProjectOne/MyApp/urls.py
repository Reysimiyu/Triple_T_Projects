from django.urls import path
from . import views

urlpatterns=[
    path('',views.Home, name='home'),
    path('create/',views.Stud, name='studForm'),
    path('addStd',views.registerStd,name='addStd'),
    path('fetchStd/',views.fetchStd,name="fetchstd")

]