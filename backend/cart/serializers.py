from .models import Cart, CartItem
from rest_framework.views import APIView
from rest_framework import serializers


class CartItemWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', "product", "quantity"]


    def create(self, validated_data):
        user = self.context['request'].user
        cart, created = Cart.objects.get_or_create(user=user)
        validated_data['cart'] = cart
        return super().create(validated_data)



class CartItemReadSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    class Meta:
        model = Cart
        fields = ['id', 'product', 'product']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemReadSerializer(many=True, read_only=True)
    class Meta:
        model = Cart
        fields = ['items']

