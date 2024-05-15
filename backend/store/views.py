from django.http import Http404
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view
from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class CategoryView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

class CategoryDetailView(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()
    


class ProductView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def get_products_by_category(self,request, category):
        queryset = Product.objects.filter(category=category)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductDetailView(APIView):
    def get_object(self,pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        try:
            product.delete()
            return Response(status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            raise Http404




# @api_view(['get'])
# def category_view(request):
#     if request.method == 'GET':
#         try:
#             categories = Category.objects.all()
#             serializer = CategorySerializer(categories, many=True)
#             return Response(serializer.data)
#         except Exception as e:
#             return Response(f"Error: {e}")
#
#
# @api_view(['post', 'GET'])
# def product_view(request):
#     if request.method == 'POST':
#         try:
#             serializer = ProductSerializer(data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response(f"Error: {e}")
#     elif request.method == 'GET':
#         try:
#             products = Product.objects.all()
#             serializer = ProductSerializer(products, many=True)
#             return Response(serializer.data)
#         except Exception as e:
#             return Response(f"Error: {e}")

