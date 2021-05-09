from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path('',views.loginuser ,name='home'),
    path('registeriuser/',views.registeruser,name='registeruser'),
    path('loginuser/',views.loginuser,name='loginuser'),
    path('userpage/',views.userpage,name='userpage'),
    path('logout_user/',views.logoutuser,name='logoutuser'),
    path('viewphoto/<slug:pk>/',views.viewphoto,name='viewphoto'),
    path('addphoto/',views.addphoto,name='addphoto'),
    path('deleteimage/<int:pk>/',views.deleteimage,name='deleteimage'),
]
