from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login , logout, authenticate
from django.contrib import messages
from .forms import *

# Create your views here.

def Userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')

        else:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})     
    return render(request, "login.html")


def logout(request):
    user = request.user
    if user.is_authenticated:
        logout(request)
        messages.success(request, "Thank you for visiting us!")
    else:
        messages.error(
            request, "You need to be logged in to perform this action")

    return redirect(reverse("login"))

def dashboard(request):
    return render(request, "index.html")

def agentDashboard(request):
    return render(request, "index.html")