from django.contrib import admin

from shop.models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(SubCategory)
admin.site.register(Category)