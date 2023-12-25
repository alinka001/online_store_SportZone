import pytest
from django.urls import reverse
from django.contrib.auth.models import User

from cart.models import CartItem, Cart
from orders.models import Order
from store.models import Item




# !!!!!!!!!!
@pytest.mark.django_db
def test_create_order(client, admin_user):
    cart = Cart.objects.create(user=admin_user)
    item = Item.objects.create(title='Test item', slug='test-item', price=100)
    cart_item = CartItem.objects.create(cart=cart, item=item, quantity=1)
    client.force_login(admin_user)
    response = client.post(reverse('checkout:create_order'), {
        'payment_method': 'card',
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com',
        'phone': '+1234567890',
        'city': 'New York',
        'street': 'Test Street',
        'street_number': '123',
        'code': '10001',
        'floor': '2',
        'entrance': '1',
        'flat': '2',
        'comment': 'Test comment',
    })
    assert Order.objects.count() == 1
    assert CartItem.objects.count() == 0