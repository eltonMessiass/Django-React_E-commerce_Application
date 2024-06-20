from django.shortcuts import render
from .serializers import ProductPriceUpdateSerializer, ProductWriteSerializer, ProductReadSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from .models import Product
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductWriteSerializer
    permission_classes = [IsAuthenticated]

class ProductDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductWriteSerializer
    permission_classes = [IsAdminUser]

class ProductPriceUpdateView(APIView):
    permission_classes = [IsAdminUser]

    def patch(self, request, pk, format=None):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        serializer = ProductPriceUpdateSerializer(product, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)