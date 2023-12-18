from django.shortcuts import get_object_or_404, render

from .models import *
from .paginator import paginator


def shop(request):
    items = Product.objects.filter(is_available=True)
    context = {
        'page_obj': paginator(request, items, 9),
        'range': [*range(1, 7)],  # For random css styles
    }

    return render(request, 'shop/main_page.html', context)


def product_details(request, item_slug):
    item = get_object_or_404(Product, slug=item_slug)
    context = {
        'item': item,
    }
    return render(request, 'shop/item_details.html', context)


# def tag_details(request, slug):
#     tag = get_object_or_404(ItemTag, slug=slug)
#     items = Product.objects.filter(tags__in=[tag])
#     context = {
#         'tag': tag,
#         'page_obj': paginator(request, items, 3),
#     }
#     return render(request, 'shop/tag_details.html', context)


def subcategory_list(request):
    tags = Product.objects.all()
    context = {
        'page_obj': paginator(request, tags, 6),
    }
    return render(request, 'shop/tag_list.html', context)
