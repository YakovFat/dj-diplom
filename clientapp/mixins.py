from django.http import HttpResponseRedirect

from clientapp.models import Cart, Product, Category, Article, AnonymousReviews
from django.shortcuts import get_object_or_404


class UniversalMixin:

    def get_cart(self, *args, **kwargs):
        cart = None
        if self.request.user.is_active:
            cart = Cart.objects.filter(user=self.request.user)
            cart = cart[0] if cart else None
        return cart

    def get_product_category_name(self, product):
        return Product.objects.filter(category__name=product)

    def get_product_category_slug(self, slug):
        return Product.objects.filter(category__slug=slug)

    def get_product_slug(self, slug):
        return get_object_or_404(Product, slug=slug)

    def get_category(self):
        return Category.objects.all()

    def get_article(self):
        return Article.objects.order_by('-date_creation')

    def anonymous_reviews(self, product):
        return AnonymousReviews.objects.filter(product=product)

    def get_context(self):
        context = {
            'category': self.get_category(),
            'cart': self.get_cart(),
        }
        return context


class CommandMixin:
    command = None

    def get(self, request, slug, *args, **kwargs):
        cart = Cart.objects.get_or_create(user=request.user)[0]
        product = Product.objects.get(slug=slug)
        if self.command == 'add':
            cart.add_to_cart(product.slug)
        elif self.command == 'remove':
            cart.remove_from_cart(product.slug)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
