from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('checkout/', include('orders.urls')),
    path('users/', include('users.urls')),
    path('', include('store.urls')),
    path('', include('django.contrib.auth.urls')),
    path('/favorites/', include('favs.urls')),
    path('manager/', include('manager_panel.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)