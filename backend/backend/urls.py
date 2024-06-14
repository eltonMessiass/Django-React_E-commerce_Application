from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = ([
    path('admin/', admin.site.urls),
    path('api/user/', include('users.urls')),
    path('api/products/', include('products.urls')),
    path('api/categories/,', include('categories.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/store/', include('store.urls')),
    path('api-auth/', include('rest_framework.urls')),
]) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
