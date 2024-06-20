from django.urls import path
from .views import ProductListCreateView, ProductPriceUpdateView


urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name="list_and_create"),
    path('products/<int:pk>/update-price/', ProductPriceUpdateView.as_view(), name="product-price-update")
]