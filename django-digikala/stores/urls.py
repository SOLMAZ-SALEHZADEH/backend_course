from django.urls import path, include
from .views import *

urlpatterns = [
    path('seller_panel/', seller_panel_view, name='seller_panel'),
    path('create_store/', create_store_view, name='create_store'),
    path('<int:store_id>/create_product/', create_Product_view, name='create_product'),
    path('<int:store_id>/store_detail/', store_detail_view, name='store_detail'),
    path('', stores_view, name='stores'),
    path('<int:store_id>/edit_product/<int:product_id>/', edit_product_view, name='edit_product'),
]