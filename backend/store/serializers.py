from .models import Category, Product, Order
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()
    class Meta:
        model = Order
        fields = ["id", "customer", "status", "created_at"]
        extra_Kwargs = {"created_at":{"read_only":True}}