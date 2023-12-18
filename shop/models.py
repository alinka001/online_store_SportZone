from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название',)

    class Meta:
        verbose_name = _("Категория")
        verbose_name_plural = _("Категории")


class SubCategory(models.Model):
    image = models.ImageField(upload_to='categories/', verbose_name='Изображение', blank=True)
    title = models.CharField(max_length=200, verbose_name='Название', )

    class Meta:
        verbose_name = _("Подкатегория")
        verbose_name_plural = _("Подкатегории")


class Product(models.Model):
    sub_category = models.ForeignKey(SubCategory, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='Название',)
    description = models.TextField(verbose_name='Описание',)
    slug = models.CharField(unique=True, max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Новая цена')
    old_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Старая цена',
                                    blank=True, null=True)
    image = models.ImageField(verbose_name='Изображение', upload_to='items/', blank=True)
    is_available = models.BooleanField(default=True, verbose_name='Доступно')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-price']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
