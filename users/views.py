from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        age = request.POST['age']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        
        # Create a new user
        user = User(first_name=first_name, last_name=last_name, username=username,
                    email=email, age=age, phone_number=phone_number, password=password)
        user.save()
        
        messages.success(request, 'Registration successful! You can now log in.')
        return redirect('login')
    
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = User.objects.get(email=email, password=password)
            messages.success(request, 'Login successful! Welcome, ' + user.first_name + '!')
            return redirect('home')  # Replace 'home' with the URL name of your home page
        except User.DoesNotExist:
            messages.error(request, 'Invalid email or password. Please try again.')
    
    return render(request, 'login.html')
