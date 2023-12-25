from django.contrib.auth.models import User
from django.db import models
from store.models import Item


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites', verbose_name='Покупатель',)

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'

    def __str__(self):
        return f"Favorites {self.id} for {self.user.username}"


class FavoritesItem(models.Model):
    favorites = models.ForeignKey(Favorites, on_delete=models.CASCADE, related_name='items', verbose_name='Избранное')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Товар')

    class Meta:
        verbose_name = 'Товар в избранном'
        verbose_name_plural = 'Товары в избранном'

    def __str__(self):
        return f"{self.item.title} in Favorites {self.favorites.id}"
