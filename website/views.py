""" views module of website app"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from website.models import Record
from .forms import SignUpForm
# Create your views here.


def home(request):
    """ home page view"""
    # Get all of the Record objects
    # pylint: disable=E1101
    records = Record.objects.all()
    # check if the user is logged in
    if request.method == 'POST':
        # do something
        username = request.POST['username']
        password = request.POST['password']
        # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in")
            return redirect('home')
        else:
            messages.success(request, "There was an error logged in")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})


def logout_user(request):
    """"Logout function"""
    logout(request)
    messages.success(request, "You have logged out")
    return redirect('home')


def register_user(request):
    """registering user function"""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # authenticate
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfuly Registered")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})
