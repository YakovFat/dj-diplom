from django.urls import path

from .views import *

urlpatterns = [ 
    path('cart/', view_cart, name='cart'),
    path('empty_section/', view_empty_section, name='empty_section'),
    path('index/', view_index, name='index'),
    path('login/', view_login, name='login'),
    path('phone/', view_phone, name='phone'),
    path('smartphones/', view_smartphones, name='smartphones'),
]