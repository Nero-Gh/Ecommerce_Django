from django.shortcuts import render,HttpResponse

# Create your views here.


def register(request):
    return HttpResponse('Register')

def login(request):
    return HttpResponse('login')

def logout(request):
    return HttpResponse('logout')