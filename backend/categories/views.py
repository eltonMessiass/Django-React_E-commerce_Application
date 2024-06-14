from django.shortcuts import render
from .models import Category
from .serializers import CategorySerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated





class CategoryListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else: 
            return (serializer.errors)
        
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
