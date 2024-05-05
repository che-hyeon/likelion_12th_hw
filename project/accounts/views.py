from django.shortcuts import render, redirect
from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.

def login(request):
    if request.method == 'POST':
        pass
    
    elif request.method == 'GET':
        return render(request, 'accounts/login.html')

def login(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('main:post')
        else:
            return render(request, 'accounts/login.html')
    
    elif request.method == 'GET':
        return render(request, 'accounts/login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('main:post')

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password']
            )
            address = request.POST['address']
            address_num = request.POST['address_num']

            profile = Profile(user=user, address=address, address_num=address_num)
            profile.save()

            auth.login(request, user)
            return redirect('/')
    return render(request, 'accounts/signup.html')