from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from cart.views import Cart
from .forms import OrderCreateForm
from .models import Order, OrderItem, ShippingAddress


@login_required
def checkout(request):
    """
    Представление чекаута.
    """
    cart = Cart.objects.get(user=request.user)
    form = OrderCreateForm()
    context = {'cart': cart, 'form': form}

    return render(request, 'orders/checkout.html', context)


@login_required
def thank_you(request, order_id):
    """
    Страница благодарности за заказ.
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/thank_you.html', {'order': order})


@login_required
def create_order(request):
    """
    Создание экземпляров Order и ShippingAddress
    из формы и редирект в профиль пользователя,
    либо передаем форму обратно.
    """
    cart = get_object_or_404(Cart, user=request.user)

    if cart.items.exists() and request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                payment_method=form.cleaned_data['payment_method'],
                user=request.user,
            )

            ShippingAddress.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                city=form.cleaned_data['city'],
                street=form.cleaned_data['street'],
                street_number=form.cleaned_data['street_number'],
                code=form.cleaned_data['code'],
                floor=form.cleaned_data['floor'],
                entrance=form.cleaned_data['entrance'],
                flat=form.cleaned_data['flat'],
                comment=form.cleaned_data['comment'],
                order=order,
            )

            for cart_item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    item=cart_item.item,
                    quantity=cart_item.quantity,
                    price=cart_item.item.price
                )

            cart.clear()
            return redirect('checkout:thank_you', order_id=order.id)
    else:
        form = OrderCreateForm()
    messages.warning(
        request, 'Форма не была корректно обработана, введите данные еще раз')
    context = {'form': form, 'cart': cart}
    return render(request, 'orders/checkout.html', context)
