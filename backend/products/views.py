from django.shortcuts import render
from .serializers import ProductPriceUpdateSerializer, ProductWriteSerializer, ProductReadSerializer
from rest_framework import generics
from .models import Product
from rest_framework.permissions import IsAuthenticated


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductWriteSerializer
    permission_classes = [IsAuthenticated]