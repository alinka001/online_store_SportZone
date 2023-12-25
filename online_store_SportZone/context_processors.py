from cart.models import CartItem, Cart
from django.contrib.auth.models import User
from django.db.models import Sum


def cart_counter(request):
    if request.user.is_authenticated:
        user = User.objects.get(pk=request.user.id)
        carts = Cart.objects.filter(user=user)
        cart_item_count = carts.annotate(total_items=Sum('items__quantity')).aggregate(total_cart_items=Sum('total_items'))
    else:
        cart_item_count = None
    return {'cart_item_count': cart_item_count}
