import pytest
from django.urls import reverse
from .models import FavoritesItem, Item, Favorites


@pytest.mark.django_db
def test_add_to_favorites(client, admin_user):
    item = Item.objects.create(title='Test item', slug='test-item', price=100)
    client.force_login(admin_user)
    response = client.get(reverse('favs:add_to_favorites', args=[item.slug]))
    assert FavoritesItem.objects.count() == 1
    favorite_item = FavoritesItem.objects.first()
    assert favorite_item.item == item
    assert favorite_item.favorites.user == admin_user


@pytest.mark.django_db
def test_delete_favorite_item(client, admin_user):
    item = Item.objects.create(title='Test item', slug='test-item', price=100)
    favorites, _ = Favorites.objects.get_or_create(user=admin_user)
    favorite_item, _ = FavoritesItem.objects.get_or_create(
        favorites=favorites,
        item=item
    )
    client.force_login(admin_user)
    response = client.get(reverse('favs:delete_favorite_item', args=[item.slug]))
    assert FavoritesItem.objects.count() == 0