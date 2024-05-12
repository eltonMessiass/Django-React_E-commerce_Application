from django.contrib import admin
from .models import *
from .models import Product, Order, Category, OrderItem


admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Category)
admin.site.register(Product)