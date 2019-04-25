from django.urls import path

from .views import *

urlpatterns = [ 
    path('', view_index, name='index'),
    path('empty_section/', view_empty_section, name='empty_section'),
    path('phone/', view_phone, name='phone'),
    path('smartphones/', view_smartphones, name='smartphones'),
    path('cart/', view_cart, name='cart'),
    path('login/', view_login, name='login'),
    path('logout/', view_logout, name='logout'),
    path('smartphones/<str>', view_smartphones, name='smartphones'),
]