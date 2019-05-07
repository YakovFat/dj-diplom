from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from clientapp.models import Product, Category, Cart, CartItem, Article


def view_index(request):
    category = Category.objects.all()
    smart = Product.objects.filter(category__name='Смартфоны')
    clothes = Product.objects.filter(category__name='Одежда')
    if request.user.is_active:
        cart = Cart.objects.filter(user=request.user)[0]
    else:
        cart = None
    article = Article.objects.order_by('-date_creation')
    context = {
        'smart': smart,
        'category': category,
        'clothes': clothes,
        'cart': cart,
        'article': article
    }
    return render(request, 'clientapp/index.html', context)


def view_cart(request):
    category = Category.objects.all()
    if request.user.is_active:
        cart = Cart.objects.filter(user=request.user)[0]
    else:
        cart = None
    context = {
        'category': category,
        'cart': cart,
    }
    return render(request, 'clientapp/cart.html', context)


def view_empty_section(request):
    if request.user.is_active:
        cart = Cart.objects.filter(user=request.user)[0]
    else:
        cart = None
    category = Category.objects.all()
    context = {
        'category': category,
        'cart': cart,
    }
    return render(request, 'clientapp/empty_section.html', context)


def view_product(request, slug):
    if request.user.is_active:
        cart = Cart.objects.filter(user=request.user)[0]
    else:
        cart = None
    category = Category.objects.all()
    product = Product.objects.get(slug=slug)
    context = {
        'product': product,
        'category': category,
        'cart': cart,
    }
    return render(request, 'clientapp/product.html', context)


def view_category(request, slug):
    if request.user.is_active:
        cart = Cart.objects.filter(user=request.user)[0]
    else:
        cart = None
    category = Category.objects.all()
    product = Product.objects.filter(category__slug=slug)
    paginator = Paginator(product, 1)
    page = request.GET.get('page')
    product_p = paginator.get_page(page)
    name_category = category.get(slug=slug)
    context = {
        'category': category,
        'product': product_p,
        'name_category': name_category,
        'cart': cart,
    }
    return render(request, 'clientapp/category.html', context)


def add_to_cart_view(request, slug):
    cart = Cart.objects.get_or_create(user=request.user)[0]
    product = Product.objects.get(slug=slug)
    cart.add_to_cart(product.slug)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_from_cart_view(request, slug):
    cart = Cart.objects.filter(user=request.user)[0]
    product = Product.objects.get(slug=slug)
    cart.remove_from_cart(product.slug)
    return redirect('cart')


def change_number_product_view(request, slug):
    product = Product.objects.get(slug=slug)
    cart_item = CartItem.objects.filter(product=product)[0]
    qty = request.POST.get('qty')
    cart_item.change_number_product(qty)
    return redirect('cart')


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
