# usermodule/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from .models import Account

def register_view(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'You have successfully registered.')
        return redirect('login')
    return render(request, 'usermodule/register.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        try:
            user = Account.objects.get(username=username)
            if user.check_password(password):
                request.session['user_id'] = user.id
                messages.success(request, 'Login successful.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid password.')
        except Account.DoesNotExist:
            messages.error(request, 'User not found.')
    return render(request, 'usermodule/login.html', {'form': form})



def login_view(request):
    form = LoginForm(request.POST or None)
    
    # If user is already logged in, pass that info to template
    user_logged_in = 'user_id' in request.session

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        try:
            user = Account.objects.get(username=username)
            if user.check_password(password):
                request.session['user_id'] = user.id
                messages.success(request, 'Login successful.')
                return redirect('login')
            else:
                messages.error(request, 'Invalid password.')
        except Account.DoesNotExist:
            messages.info(request, 'User not found. Please register.')
            return redirect('register')
    
    return render(request, 'usermodule/login.html', {'form': form, 'user_logged_in': user_logged_in})

def logout_view(request):
    request.session.flush()
    messages.info(request, 'You have been logged out.')
    return redirect('login')

def home_view(request):
    return render(request, 'usermodule/home.html')