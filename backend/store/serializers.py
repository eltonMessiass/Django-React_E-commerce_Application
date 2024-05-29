from .models import Category, Product, Order, OrderItem
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "image_url"]

    def get_image_url(self, obj:Product):
        if obj.image:
            return obj.image.url
        return None



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