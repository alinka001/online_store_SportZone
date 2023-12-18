from django.db import models

# сделать чтобы для товара выбиралось только нужная подкатегория
#из категорий


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название',)

    def __str__(self):
        return self.title

    # def get_subcategory(self):
    #     subcategory_objects = SubCategory.objects.filter(subcategory_category=self)
    #     return subcategory_objects

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='categories/', verbose_name='Изображение', blank=True)
    title = models.CharField(max_length=200, verbose_name='Название', )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Product(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
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
