from django.urls import path
from . import views

urlpatterns=[
    path('',views.Home, name='home'),
    path('create/',views.Stud, name='studForm'),
    path('addStd',views.registerStd,name='addStd'),
    path('fetchStd/',views.fetchStd,name="fetchstd"),
    path('updateStd/<int:pk>',views.updateStd,name="updatestd"),
    path('deleteStd/<int:pk>',views.deleteStd,name="deletestd"),
    path('signup/',views.userRegistration,name='signup'),
    path('signin/',views.login_view,name='signin'),
    path('signout/',views.logout_view,name='signout')


]