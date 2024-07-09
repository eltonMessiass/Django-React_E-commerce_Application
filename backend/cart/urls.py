from django.urls import path
from .views import CartItemView, UserCartView, CartItemDetaitlView

urlpatterns = [
    path("cart/", UserCartView.as_view(), name="items"),
    path("cart_detail/<int:pk>/", CartItemDetaitlView.as_view(), name="cart_detail")
]