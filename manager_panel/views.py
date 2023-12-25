from django.shortcuts import render, redirect

from store.forms import ItemTagForm
from store.models import Item, ItemTag
from django.shortcuts import render


def tag_list_manager(request):
    tags = ItemTag.objects.all()
    context = {
        'tags': tags
    }
    return render(request, 'panel/tag_list_manager.html', context)


def add_tag(request):
    if request.method == 'POST':
        form = ItemTagForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manager:tag_list_manager')
    else:
        form = ItemTagForm()
    return render(request, 'panel/add_tag.html', {'form': form})


def delete_tag(request, tag_slug):
    tag = ItemTag.objects.get(slug=tag_slug)
    tag_id = tag.id
    items = Item.objects.filter(tags=tag_id)
    items.delete()
    tag.delete()
    return redirect('manager:tag_list_manager')


'''items'''


def items_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'panel/items.html', context)
