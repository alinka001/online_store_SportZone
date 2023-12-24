from django.urls import path

from .views import favorites, add_to_favorites, delete_favorite_item

app_name = 'favs'

urlpatterns = [
    path('', favorites, name='favorites'),
    path('add/<slug:item_slug>/', add_to_favorites, name='add_to_favorites'),
    path('delete/<slug:item_slug>/', delete_favorite_item, name='delete_favorite_item'),
    # path('update_cart_item/', update_cart_item, name='update_cart_item'),
]
