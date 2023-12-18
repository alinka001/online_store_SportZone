from django.urls import path

from .views import product_details, shop,  subcategory_list

app_name = 'shop'


urlpatterns = [
    path('', shop, name='home'),
    path('categories/', subcategory_list, name='product_list'),
    #path('category-details/<slug:slug>/', tag_details, name='tag_details'),
    path('<slug:product_slug>/', product_details, name='product_details'),
]
