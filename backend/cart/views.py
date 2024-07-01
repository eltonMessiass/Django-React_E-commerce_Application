from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import CartItemWriteSerializer, CartItemReadSerializer
from rest_framework.response import Response
from  rest_framework import status
from .models import CartItem




class CartItemView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = CartItemWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        cartItems = CartItem.objects.all()
        serializer = CartItemReadSerializer(cartItems)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

#update the quantity or remove the item from the cart
class CartItemDetaitlView(APIView):
    def get_object(self, pk):
        try:
            return CartItem.objects.get(pk=pk)
        except CartItem.DoesNotExist:
          raise Http404
        
    def delete(self, request, pk, format=None):
        item = self.get_object(pk)
        item.delete()
        return Response("item removed", status=status.HTTP_204_NO_CONTENT)
   
    def update(self, request, pk, format=None):
        try:
            item = self.get_object(pk)
            quantity = request.data.get('quantity')

            if quantity is None:
                return Response({'error':'Quantity is required'}, status=status.HTTP_400_BAD_REQUEST)        
            if quantity <= 0:
                return Response({'error': 'Quantity must be greater than zero'}, status=status.HTTP_400_BAD_REQUEST)
              
            item.quantity = quantity
            item.save()

            return Response({'status': 'quantity updated'}, status=status.HTTP_200_OK)
        except CartItem.DoesNotExist:
            return Response({'error': 'Cart item not found'}, status=status.HTTP_404_NOT_FOUND)


        

