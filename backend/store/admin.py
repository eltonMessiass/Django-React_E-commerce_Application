from django.contrib import admin
from .models import *
from .models import Product, Order, Category, OrderItem, Cart, CartItem


admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)