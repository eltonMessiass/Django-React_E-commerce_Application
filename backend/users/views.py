from django.shortcuts import render
from .serializers import UserSerializer
from django.contrib.auth.models import User
from .models import CustomerUser
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated


class CreateUserView(generics.CreateAPIView):
    queryset = CustomerUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class ListUsersView(generics.ListAPIView):
    queryset = CustomerUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]