from django.urls import path

from .views import add_to_cart, cart, delete_cart_item, plus_cart_item, minus_cart_item

app_name = 'cart'

urlpatterns = [
    path('', cart, name='cart'),
    path('add/<slug:item_slug>/', add_to_cart, name='add_to_cart'),
    path('delete/<slug:item_slug>/', delete_cart_item, name='delete_cart_item'),
    path('plus_cart_item/<slug:item_slug>/', plus_cart_item, name='plus_cart_item'),
    path('minus_cart_item/<slug:item_slug>/', minus_cart_item, name='minus_cart_item'),
]
