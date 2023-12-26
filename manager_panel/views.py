from django.shortcuts import redirect
from django.template.defaultfilters import slugify

from store.forms import ItemTagForm, ItemForm
from store.models import Item, ItemTag
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


def admin_required(function=None, redirect_field_name=None, login_url=None):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_staff,
        redirect_field_name=redirect_field_name,
        login_url=login_url
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

@admin_required
def tag_list_manager(request):
    tags = ItemTag.objects.all()
    context = {
        'tags': tags
    }
    return render(request, 'panel/tag_list_manager.html', context)

@admin_required
def add_tag(request):
    if request.method == 'POST':
        form = ItemTagForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manager:tag_list_manager')
    else:
        form = ItemTagForm()
    return render(request, 'panel/add_tag.html', {'form': form})

@admin_required
def delete_tag(request, tag_slug):
    tag = ItemTag.objects.get(slug=tag_slug)
    tag_id = tag.id
    items = Item.objects.filter(tags=tag_id)
    items.delete()
    tag.delete()
    return redirect('manager:tag_list_manager')


'''items'''


@admin_required
def item_list_manager(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'panel/items_list_manager.html', context)


@admin_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.slug = slugify(item.title)
            item.save()
            return redirect('manager:item_list_manager')
    else:

        form = ItemForm()

    return render(request, 'panel/add_item.html', {'form': form})


@admin_required
def delete_item(request, item_slug):
    item = Item.objects.get(slug=item_slug)
    item.delete()
    return redirect('manager:item_list_manager')
