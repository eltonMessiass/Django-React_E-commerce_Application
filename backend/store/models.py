from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
    stock = models.PositiveIntegerField(null=False, blank=False, default=0)
    price = models.IntegerField(null=False, blank=False, default=0)
    description = models.TextField(null=True, blank=True, default='')

    def __str__(self):
        return self.name

    def calculate_total_price(self, quantity):
        return quantity * self.price


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.customer.username}"

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-created_at')


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.id}"