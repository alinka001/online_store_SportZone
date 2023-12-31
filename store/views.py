import random

from django.shortcuts import get_object_or_404, render

from .models import Item, ItemTag
from .paginator import paginator


def store(request):
    items = Item.objects.filter(is_sale=True)
    random_items = random.sample(list(items), 3)
    context = {
        'page_obj': paginator(request, random_items, 6)
    }

    return render(request, 'store/main_page.html', context)



def item_details(request, item_slug):
    item = get_object_or_404(Item, slug=item_slug)
    context = {
        'item': item,
    }
    return render(request, 'store/item_details.html', context)


def tag_details(request, slug):
    tag = get_object_or_404(ItemTag, slug=slug)
    items = Item.objects.filter(tags__in=[tag])
    context = {
        'tag': tag,
        'page_obj': paginator(request, items, 3),
    }

    return render(request, 'store/tag_details.html', context)


def tag_list(request):
    tags = ItemTag.objects.all()
    items = Item.objects.all()
    context = {
        'tags': tags,
        'page_obj': paginator(request, items, 6),
    }
    return render(request, 'store/tag_list.html', context)


def filtered_by_tag(request, slug):
    tags = ItemTag.objects.all()
    tag = get_object_or_404(ItemTag, slug=slug)
    items = Item.objects.filter(tags__in=[tag])
    context = {
        'tags': tags,
        'tag': tag,
        'page_obj': paginator(request, items, 3),
    }

    return render(request, 'store/filtered.html', context)
