from django.shortcuts import redirect, render
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


# Create your views here.

def index(request):
  return render(request, 'recommendation.html')
  
def firstRating(request):
  return render(request, 'first_rating.html')

def login(request):
  if request.method == 'POST':
    user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
    if user is not None:
      auth.login(request,user)
      return redirect('index')
    else:
      return render(request, 'login.html', {'error': 'username atau password masih salah'})
  else:
      return render(request, 'login.html')

def signup(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('login')
    return render(request, 'register.html', {'form': form})

def logout(request):
  auth.logout(request)
  return render(request,'logout.html')

def about(request):
  return render(request, 'about.html')