from django.contrib import admin
from .models import *
from .models import Product, Order, Category

admin.site.register(Product.Product)
admin.site.register(Order.Order)
admin.site.register(Category.Category)
