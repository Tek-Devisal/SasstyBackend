from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cart.serializers import CartSerializer
from rest_framework import status

@api_view(['POST'])
def addToCart(request, format=None):
    if request.method == 'POST':

        serializer = CartSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

