from django.urls import path
from .views import *

urlpatterns = [
    path('add_to_cart/<int:product_id>/', add_to_cart_view, name='add_to_cart'),
    path('cart/', cart_view, name='cart'),
    path(
    'remove_from_cart/<int:product_id>/',
    remove_from_cart,
    name='remove_from_cart'
),
    path(
    'checkout/',
    checkout_view,
    name='checkout'
),
path('payment/', add_balance_view, name='payment'),
path('order_history/', order_history_view, name='order_history'),
]