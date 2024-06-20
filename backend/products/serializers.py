from .models import Product
from categories.serializers import CategorySerializer
from rest_framework import serializers


class ProductReadSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = Product
        fields = ["id", "name", "description", "price", "category", "stock"]


class ProductWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "category", "stock"]
        extra_Kwargs = {
            'name': {'required':True},
            'category': {'required': True}
        }


class ProductPriceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["price"]
        extra_Kwargs = {
            "price": {"required": True, 'min_value':0}
        }