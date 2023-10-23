""" views module of website app"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def home(request):
    """ home page view"""
    # check if the user is logged in
    if request.method == 'POST':
        # do something
        username = request.POST['username']
        password = request.POST['password']
        # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have logged int")
            return redirect('home')
        else:
            messages.success(request, "There was an error logged in")
            return redirect('home')
    else:
        return render(request, 'home.html', {})


def logout_user(request):
    """"Logout function"""
    logout(request)
    messages.success(request, "You have logged out")
    return redirect('home')


def register_user(request):
    """registering user function"""
    return render(request, 'register.html', {})
