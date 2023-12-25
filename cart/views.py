from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt

from store.models import Item
from .models import Cart, CartItem


@login_required
def cart(request):
    """
    Представление для вывода всех объектов
    товаров корзины и самой корзины.
    """
    cart = Cart.objects.filter(user=request.user).first()

    if not cart:
        cart = Cart.objects.create(user=request.user)

    context = {
        'cart_items': CartItem.objects.filter(cart=cart),
        'cart': cart
    }

    return render(request, 'cart/cart.html', context)


@login_required
def add_to_cart(request, item_slug):
    """
    Представление для добавления товара в корзину
    либо увеличения его количества на 1.
    """
    item = get_object_or_404(Item, slug=item_slug)
    cart, _ = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        item=item
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart:cart')




@login_required
def delete_cart_item(request, item_slug):
    """
    Представление для удаления объекта товара в корзине.
    """
    cart_item = CartItem.objects.get(
        cart=Cart.objects.get(user=request.user),
        item=get_object_or_404(Item, slug=item_slug)
    )
    cart_item.delete()
    return redirect('cart:cart')


@login_required
def plus_cart_item(request, item_slug):
    cart_item = CartItem.objects.get(
        cart=Cart.objects.get(user=request.user),
        item=get_object_or_404(Item, slug=item_slug)
    )
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:cart')

@login_required
def minus_cart_item(request, item_slug):
    cart_item = CartItem.objects.get(
        cart=Cart.objects.get(user=request.user),
        item=get_object_or_404(Item, slug=item_slug)
    )
    cart_item.quantity -= 1
    cart_item.save()
    return redirect('cart:cart')