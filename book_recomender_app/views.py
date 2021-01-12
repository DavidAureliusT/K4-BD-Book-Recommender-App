from django.http import HttpResponse
from django.shortcuts import render

#function view
def index(request):
  return render(request, 'index2.html')

def index2(request):
  return render(request, 'index.html')
  
def about(request):
  return render(request, 'about.html')

def login(request):
  return render(request, 'login.html')

def register(request):
  return render(request, 'register.html')