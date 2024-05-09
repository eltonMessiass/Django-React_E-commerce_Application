from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {"password": {"write_only": True}}

        @staticmethod
        def create(validated_data):
            user = User.objects.create_user(**validated_data)
            return user

