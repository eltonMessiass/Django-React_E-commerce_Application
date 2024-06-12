from .models import Category, Product, Order, OrderItem, Cart, CartItem
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

class CartItemsSerializer(serializers.ModelSerializer):
    # product = serializers.StringRelatedField()
    class Meta:
        model = CartItem
        fields = ["id", "product", "quanity"]
    
    def create(self, validated_data):
        user = self.context['request'].user
        cart, created = user.cart, Cart.objects.get_or_create(user=user)
        validated_data['cart'] = cart
        return super().create(validated_data)

class CartSerializer(serializers.ModelSerializer):
    items = CartItemsSerializer(many=True, read_only=True)
    class Meta:
        model = Cart
        fields = ["items"]


class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
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