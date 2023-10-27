""" views module of website app"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from website.models import Record
from .forms import SignUpForm, AddRecordForm
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


def user_record(request, pk):
    """view users record method"""
    if request.user.is_authenticated:
        # look up the user record
        # pylint: disable=E1101
        user_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'user_record': user_record})
    else:
        messages.success(request, "You Must Login to View User")
        return redirect('home')


def delete_record(request, pk):
    """delete record method"""
    if request.user.is_authenticated:
        # pylint: disable=E1101
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "You Have deleted User Suceessfully")
        return redirect('home')
    else:
        messages.success(request, "You Must be Logged in to delete a User")
        return redirect('home')


def add_record(request):
    """adding new record function"""
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "New Record Added Successfully...")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, "You must e logged in  to add a record...")
        return redirect('home')


def update_record(request, pk):
    """Updating record view function"""
    if request.user.is_authenticated:
        # pylint: disable=E1101
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Record has been Updated Successfully...")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, "You must e logged in  to add a record...")
        return redirect('home')
