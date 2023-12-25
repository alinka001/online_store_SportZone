from django.urls import path

from .views import item_details, store, tag_details, tag_list, filtered_by_tag

app_name = 'store'


urlpatterns = [
    path('', store, name='home'),
    path('categories/', tag_list, name='tag_list'),
    path('category-details/<slug:slug>/', tag_details, name='tag_details'),
    path('<slug:item_slug>/', item_details, name='item_details'),
    path('filtered_by_tag/<slug:slug>/', filtered_by_tag, name='filtered_by_tag'),

]
