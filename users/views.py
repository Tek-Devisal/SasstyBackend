# from rest_framework.viewsets import GenericViewSet
# from rest_framework.mixins import CreateModelMixin
# from django.contrib.auth import get_user_model
# from rest_framework.decorators import api_view
# from rest_framework import status

from rest_framework import generics, permissions
from rest_framework.response import Response
# from knox.models import AuthToken
from .serializers import UserSerializer

# Register API
class Register(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = []