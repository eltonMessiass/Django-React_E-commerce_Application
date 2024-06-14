from django.http import Http404
from rest_framework import status, generics
from .serializers import CategorySerializer, ProductSerializer,OrderSerializer, OrderItemSerializer, CartItemsSerializer, CartSerializer
from .models import Category, Product, Order, OrderItem, Cart, CartItem
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny



class CategoryListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)
        

    
class ProductListCreate(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors)

class ProductListByCategory(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        products = Product.objects.filter(category=category)
        return products
     

class ProductView(APIView):
    permission_classes=[AllowAny]
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

class CartItemsCreate(generics.CreateAPIView):
    serializer_class = CartItemsSerializer
    permission_classes = [IsAuthenticated]

class CartList(generics.ListAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

class OrderView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        if user.is_authenticated:  
            order = Order.objects.filter(customer=user)
            serializer = OrderSerializer(order, many=True)
            return Response(serializer.data)
        else:
            return Response({"detail": "Authentication credentials were not provided."}, status=401)

    
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderItemView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()


