from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.
def home(request):
    return render(request, 'djangoapp/index.html')


# Create an `about` view to render a static about page
# def about(request):
# ...
def about(request):
    return render(request, 'djangoapp/about.html')



# Create a `contact` view to return a static contact page
#def contact(request):
def contact(request):
    return render(request, 'djangoapp/contact.html')

# Create a `login_request` view to handle sign in request
# def login_request(request):
# ...
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or another view
            messages.success(request, 'Login successful.')
            return redirect('djangoapp:home')  # Redirect to the home page after successful login
        else:
            # Display an error message for failed login
            messages.error(request, 'Invalid username or password. Please try again.')

    # Render the login form
    return render(request, 'djangoapp/login.html')  # Create a login.html template for the login form

# Create a `logout_request` view to handle sign out request
# def logout_request(request):
# ...
def user_logout(request):
    logout(request)
    # Redirect to a page after logout or another view
    return redirect('djangoapp:home')  # Redirect to the home page after logout

# Create a `registration_request` view to handle sign up request
# def registration_request(request):
# ...
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully. Please log in.')
            return redirect('auth:login')  # Redirect to the login page after successful signup
        else:
            # Handle form validation errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")

    else:
        form = UserCreationForm()
    
    return render(request, 'djangoapp/registration.html', {'form': form})

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

