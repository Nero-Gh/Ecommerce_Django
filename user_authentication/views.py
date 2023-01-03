from django.shortcuts import render,redirect

# Create your views here.


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
    else:
        print('get World')

    return render(request, 'authentication/register.html')

def login(request):
    return render(request, 'authentication/login.html')

def logout(request):
    return redirect('user-login')