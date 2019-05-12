from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from clientapp.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [ 
    path('', IndexView.as_view(), name='index'),
    path('empty_section/', EmptySectionView.as_view(), name='empty_section'),
    path('product/<slug:slug>/', ProductView.as_view(), name='product'),
    path('cart/', CartView.as_view(), name='cart'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('category/<slug:slug>/', CategoryView.as_view(), name='category'),
    path('add_to_cart/<slug:slug>', AddToCartView.as_view(), name='add_to_cart'),
    path('remove_from_cart/<slug:slug>', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('change_number_product/<slug:slug>', ChangeNumberProductView.as_view(),
         name='change_number_product'),
    path('order_registration/', OrderRegistrariomView.as_view(), name='order_registration'),
    path('registration/', RegisterView.as_view(), name='registration'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)