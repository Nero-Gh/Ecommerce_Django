from django.shortcuts import render,redirect

# Create your views here.


def register(request):
    return render(request, 'authentication/register.html')

def login(request):
    return render(request, 'authentication/login.html')

def logout(request):
    return redirect('user-login')