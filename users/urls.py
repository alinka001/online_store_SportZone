from django.contrib.auth.views import LoginView, LogoutView

from django.urls import path

from .views import SignUp, profile, user_orders

app_name = 'users'

urlpatterns = [
    path('orders/', user_orders, name='user_orders'),
    path('profile/', profile, name='profile'),
    path('auth/logout/', LogoutView.as_view(template_name='users/logged_out.html'), name='logout'),
    path('auth/signup/', SignUp.as_view(), name='signup'),
    path('auth/login/', LoginView.as_view(template_name='users/login.html'), name='login')

]
