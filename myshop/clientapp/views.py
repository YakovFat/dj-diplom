from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def view_admin(request):
    return render(request, 'clientapp/admin.html')

def view_cart(request):
    return render(request, 'clientapp/cart.html')

def view_empty_section(request):
    return render(request, 'clientapp/empty_section.html')

def view_index(request):
    return render(request, 'clientapp/index.html')

def view_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    else:
        return render(
            request,
            'clientapp/login.html',
        )

def view_logout(request):
    logout(request)
    return redirect('index')

def view_phone(request):
    return render(request, 'clientapp/phone.html')

def view_smartphones(request):
    return render(request, 'clientapp/smartphones.html')
