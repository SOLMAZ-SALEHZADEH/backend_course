from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', user_login_view, name='login'),
    path('signup/', user_register_view, name='signup'),
    path('logout/', user_logout_view, name='logout'),
    path('customer/', customer_view, name='customer'),
    path('become_seller/', become_seller_view, name='become_seller')
]