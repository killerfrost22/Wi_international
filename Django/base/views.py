from django.shortcuts import render

# Create your views here.
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return render(request,  'home.html')

def room(request):
    return render(request, 'room.html')