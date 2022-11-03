from dataclasses import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username', 'first_name', 'last_name', 'password', 'email')

    def create(self, validated_data):
        """Create and return a new user."""

        user = UserModel(
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            username = validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user