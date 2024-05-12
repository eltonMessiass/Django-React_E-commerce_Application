from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product
from rest_framework.response import Response


@api_view(['get'])
def category_view(request):
    if request.method == 'GET':
        try:
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(f"Error: {e}")


@api_view(['post', 'GET'])
def product_view(request):
    if request.method == 'POST':
        try:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(f"Error: {e}")
    elif request.method == 'GET':
        try:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(f"Error: {e}")

