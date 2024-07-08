from django.urls import path
from .views import CartItemView, UserCartView

urlpatterns = [
    path("cart/", UserCartView.as_view(), name="items"),
]