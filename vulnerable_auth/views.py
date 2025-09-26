from django.shortcuts import render, redirect
from django.db import connection
from .forms import RegistrationForm, LoginForm
from .models import InsecureUser

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'vulnerable_auth/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            with connection.cursor() as cursor:
                # This is intentionally written to be insecure
                query = f"SELECT * FROM vulnerable_auth_insecureuser WHERE username = '{username}' AND password = '{password}'"
                cursor.execute(query)
                user = cursor.fetchone()
            if user:
                # In a real app, you'd set a session here
                return redirect('welcome')
            else:
                return render(request, 'vulnerable_auth/login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = LoginForm()
    return render(request, 'vulnerable_auth/login.html', {'form': form})

def welcome(request):
    return render(request, 'vulnerable_auth/welcome.html')
