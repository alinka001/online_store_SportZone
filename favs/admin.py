from django.contrib import admin

from favs.models import Favorites, FavoritesItem

# Register your models here.
admin.site.register(Favorites)
admin.site.register(FavoritesItem)
