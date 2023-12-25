import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from cart.models import Cart, CartItem
from store.models import Item


@pytest.mark.django_db
def test_add_to_cart(client):
    user = User.objects.create_user(username='testuser', password='testpassword')
    client.login(username='testuser', password='testpassword')
    item = Item.objects.create(title='Test Item', price=9.99, slug='test')
    response = client.get(reverse('cart:add_to_cart', args=[item.slug]))
    assert response.status_code == 302
    assert response.url == reverse('cart:cart')
    cart = Cart.objects.get(user=user)
    cart_item = CartItem.objects.get(cart=cart, item=item)
    assert cart_item.quantity == 1


@pytest.mark.django_db
def test_delete_cart_item(client, admin_user):
    item = Item.objects.create(title='Test item', slug='test-item', price=100)
    cart = Cart.objects.create(user=admin_user)
    cart_item = CartItem.objects.create(cart=cart, item=item, quantity=1)
    client.force_login(admin_user)
    response = client.get(reverse('cart:delete_cart_item', args=[item.slug]))
    assert CartItem.objects.count() == 0