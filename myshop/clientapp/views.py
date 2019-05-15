from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from clientapp.models import Product, Category, Cart, Order, CartItem, AnonymousReviews
from django.views import View
from clientapp.mixins import UniversalMixin, CommandMixin
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from clientapp.forms import UserCreationForm


class IndexView(UniversalMixin, View):
    def get(self, request, *args, **kwargs):
        data_mixin = super(IndexView, self)
        smart = data_mixin.get_product_category_name('Смартфоны')
        clothes = data_mixin.get_product_category_name('Одежда')
        article = data_mixin.get_article()
        context = data_mixin.get_context()
        context['smart'] = smart
        context['clothes'] = clothes
        context['article'] = article
        return render(request, 'clientapp/index.html', context)


class CartView(UniversalMixin, View):
    def get(self, request, *args, **kwargs):
        data_mixin = super(CartView, self)
        context = data_mixin.get_context()
        return render(request, 'clientapp/cart.html', context)


class EmptySectionView(UniversalMixin, View):
    def get(self, request, *args, **kwargs):
        data_mixin = super(EmptySectionView, self)
        context = data_mixin.get_context()
        return render(request, 'clientapp/empty_section.html', context)


class ProductView(UniversalMixin, View):
    def get(self, request, slug, *args, **kwargs):
        data_mixin = super(ProductView, self)

        context = data_mixin.get_context()
        product = data_mixin.get_product_slug(slug)
        anonymous_reviews = data_mixin.anonymous_reviews(product)
        context['product'] = product
        context['anonymous_reviews'] = anonymous_reviews
        return render(request, 'clientapp/product.html', context)


class CategoryView(UniversalMixin, View):
    def get(self, request, slug, *args, **kwargs):
        data_mixin = super(CategoryView, self)
        context = data_mixin.get_context()
        product = data_mixin.get_product_category_slug(slug)
        paginator = Paginator(product, 3)
        page = request.GET.get('page')
        product_p = paginator.get_page(page)
        name_category = get_object_or_404(Category, slug=slug)
        context['product'] = product_p
        context['name_category'] = name_category
        return render(request, 'clientapp/category.html', context)


class AddToCartView(CommandMixin, View):
    command = 'add'


class RemoveFromCartView(CommandMixin, View):
    command = 'remove'


class OrderRegistrariomView(View):
    def get(self, request, *args, **kwargs):
        cart = Cart.objects.filter(user=request.user)
        if cart:
            cart = cart[0]
            order = Order()
            order.order_registration(cart, request.user)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class ChangeNumberProductView(View):
    def post(self, request, slug):
        product = Product.objects.get(slug=slug)
        cart_item = CartItem.objects.filter(product=product)[0]
        qty = request.POST.get('qty')
        cart_item.change_number_product(qty)
        return redirect('cart')


class MyLoginView(LoginView):
    template_name = 'clientapp/login.html'



class RegisterFormView(FormView):

    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "clientapp/registration.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


class AnonymousReviewsView(View):
    def post(self, request, slug):
        name = request.POST.get('name')
        description = request.POST.get('description')
        mark = request.POST.get('mark')
        if len(name) != 0 and str(mark) != 'NoneType':
            reviews = AnonymousReviews(name=name, product=Product.objects.get(slug=slug), description=description, mark=int(mark))
            reviews.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))





# def view_logout(request):
#     logout(request)
#     return redirect('index')


# def view_index(request):
#     category = Category.objects.all()
#     smart = Product.objects.filter(category__name='Смартфоны')
#     clothes = Product.objects.filter(category__name='Одежда')
#     article = Article.objects.order_by('-date_creation')
#     cart = None
#     if request.user.is_active:
#         cart = Cart.objects.filter(user=request.user)
#         cart = cart[0] if cart else None
#     context = {
#         'smart': smart,
#         'category': category,
#         'clothes': clothes,
#         'cart': cart,
#         'article': article
#     }
#     return render(request, 'clientapp/index.html', context)

# def view_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('index')
#     else:
#         return render(
#             request,
#             'clientapp/login.html',
#         )

# def view_cart(request):
#     category = Category.objects.all()
#     cart = None
#     if request.user.is_active:
#         cart = Cart.objects.filter(user=request.user)
#         cart = cart[0] if cart else None
#     context = {
#         'category': category,
#         'cart': cart,
#     }
#     return render(request, 'clientapp/cart.html', context)

# def view_empty_section(request):
#     cart = None
#     if request.user.is_active:
#         cart = Cart.objects.filter(user=request.user)
#         cart = cart[0] if cart else None
#     category = Category.objects.all()
#     context = {
#         'category': category,
#         'cart': cart,
#     }
#     return render(request, 'clientapp/empty_section.html', context)

# def view_product(request, slug):
#     cart = None
#     if request.user.is_active:
#         cart = Cart.objects.filter(user=request.user)
#         cart = cart[0] if cart else None
#     category = Category.objects.all()
#     product = Product.objects.get(slug=slug)
#     context = {
#         'product': product,
#         'category': category,
#         'cart': cart,
#     }
#     return render(request, 'clientapp/product.html', context)

# def view_category(request, slug):
#     cart = None
#     if request.user.is_active:
#         cart = Cart.objects.filter(user=request.user)
#         cart = cart[0] if cart else None
#     category = Category.objects.all()
#     product = Product.objects.filter(category__slug=slug)
#     paginator = Paginator(product, 3)
#     page = request.GET.get('page')
#     product_p = paginator.get_page(page)
#     name_category = category.get(slug=slug)
#     context = {
#         'category': category,
#         'product': product_p,
#         'name_category': name_category,
#         'cart': cart,
#     }
#     return render(request, 'clientapp/category.html', context)

#
# def add_to_cart_view(request, slug):
#     cart = Cart.objects.get_or_create(user=request.user)[0]
#     product = Product.objects.get(slug=slug)
#     cart.add_to_cart(product.slug)
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# def remove_from_cart_view(request, slug):
#     cart = Cart.objects.filter(user=request.user)[0]
#     product = Product.objects.get(slug=slug)
#     cart.remove_from_cart(product.slug)
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

#
# def order_registration_view(request):
#     cart = Cart.objects.filter(user=request.user)
#     if cart:
#         cart = cart[0]
#         order = Order()
#         order.order_registration(cart, request.user)
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# def change_number_product_view(request, slug):
#     product = Product.objects.get(slug=slug)
#     cart_item = CartItem.objects.filter(product=product)[0]
#     qty = request.POST.get('qty')
#     cart_item.change_number_product(qty)
#     return redirect('cart')



# class RegisterView(View):
    # def get(self, request):
    #     return render(request, 'clientapp/registration.html')
    # def post(self, request):
    #     if request.method == 'POST':
    #         username = request.POST['username']
    #         password1 = request.POST['password1']
    #         password2 = request.POST['password2']
    #         print(username, password1, password2)
    #     return render(request, 'clientapp/registration.html')