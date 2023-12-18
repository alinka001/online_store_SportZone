from django.urls import path

from .views import order, create_order, thank_you

app_name = 'orders'

urlpatterns = [
    path('', order, name='order'),
    path('create-order/', create_order, name='create_order'),
    path('thank-you/<int:order_id>/', thank_you, name='thank_you'),
]
