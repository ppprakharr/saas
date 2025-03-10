from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login

def login_view(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        return redirect('/')
    return render(request,'userauth/login.html',{})

# Create your views here.
