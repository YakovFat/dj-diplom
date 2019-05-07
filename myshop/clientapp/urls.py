from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from clientapp.views import *

urlpatterns = [ 
    path('', view_index, name='index'),
    path('empty_section/', view_empty_section, name='empty_section'),
    path('product/<slug:slug>/', view_product, name='product'),
    path('cart/', view_cart, name='cart'),
    path('login/', view_login, name='login'),
    path('logout/', view_logout, name='logout'),
    path('category/<slug:slug>/', view_category, name='category'),
    path('add_to_cart/<slug:slug>', add_to_cart_view, name='add_to_cart'),
    path('remove_from_cart/<slug:slug>', remove_from_cart_view, name='remove_from_cart'),
    path('change_number_product/<slug:slug>', change_number_product_view,
         name='change_number_product'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)