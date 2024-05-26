from .models import Category, Product, Order, OrderItem
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"



class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["order", "product", "quantity", "price", "subtotal"]

class OrderSerializer(serializers.ModelSerializer):
    # customer = serializers.StringRelatedField()
    items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ["id", "customer","phone", "status", "created_at", "items"]
        extra_Kwargs = {"created_at":{"read_only":True}}