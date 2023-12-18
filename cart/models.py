from django.contrib.auth.models import User
from django.db import models

from shop.models import Product


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='carts',
        verbose_name='Покупатель',
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания',)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    @property
    def total_price(self):
        total_price = sum(item.total_price for item in self.products.all())
        return total_price

    def __str__(self):
        return f"Cart {self.id} for {self.user.username}"

    def clear(self):
        self.products.all().delete()


class CartProduct(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Корзина',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Товар',
    )
    quantity = models.PositiveIntegerField(
        default=1, verbose_name='Количество',)

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    @property
    def total_price(self):
        total_price = self.quantity * self.product.price
        return total_price

    def __str__(self):
        return f"{self.quantity} x {self.product.title}"
