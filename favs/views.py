from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from store.models import Item
from .models import Favorites, FavoritesItem


@login_required
def favorites(request):
    favorites = Favorites.objects.filter(user=request.user).first()
    if not favorites:
        favorites = Favorites.objects.create(user=request.user)
    context = {
        'favorite_items': FavoritesItem.objects.filter(favorites=favorites),
        'favorites': favorites
    }
    return render(request, 'favs/favorites.html', context)


@login_required
def add_to_favorites(request, item_slug):
    item = get_object_or_404(Item, slug=item_slug)
    favorites, _ = Favorites.objects.get_or_create(user=request.user)
    favorite_item, created = FavoritesItem.objects.get_or_create(
        favorites=favorites,
        item=item
    )
    print(favorite_item)
    favorite_item.save()
    return redirect('favs:favorites')


@login_required
def delete_favorite_item(request, item_slug):
    favorite_item = FavoritesItem.objects.get(
        favorites=Favorites.objects.get(user=request.user),
        item=get_object_or_404(Item, slug=item_slug)
    )
    favorite_item.delete()
    return redirect('favs:favorites')

