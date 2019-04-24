from django.shortcuts import render

# Create your views here.
def view_admin(request):
    return render(request, 'clientapp/admin.html')

def view_cart(request):
    return render(request, 'clientapp/cart.html')

def view_empty_section(request):
    return render(request, 'clientapp/empty_section.html')

def view_index(request):
    return render(request, 'clientapp/index.html')

def view_login(request):
    print(request.POST)
    return render(
        request,
        'clientapp/login.html',
    )

def view_phone(request):
    return render(request, 'clientapp/phone.html')

def view_smartphones(request):
    return render(request, 'clientapp/smartphones.html')
