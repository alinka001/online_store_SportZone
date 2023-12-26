from django.urls import path

from . import views

app_name = 'manager'

urlpatterns = [
    path('addtag/', views.add_tag, name='add_tag'),
    path('taglist/', views.tag_list_manager, name='tag_list_manager'),
    path('delete/<slug:tag_slug>/', views.delete_tag, name='delete_tag'),
    path('itemlist/', views.item_list_manager, name='item_list_manager'),
    path('additem/', views.add_item, name='add_item'),
    path('deleteitem/<slug:item_slug>/', views.delete_item, name='delete_item'),
]