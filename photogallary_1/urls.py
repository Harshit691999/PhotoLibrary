from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path('',views.gallary,name='home'),
    path('viewphoto/<slug:pk>/',views.viewphoto,name='viewphoto'),
    path('addphoto/',views.addphoto,name='addphoto'),
    path('deleteimage/<int:pk>/',views.deleteimage,name='deleteimage'),
]
