from django.shortcuts import render
from .models import Stock
from stock.serializers import StockSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status
from random import shuffle


#STOCK
# @api_view(['POST'])
# def addStock(request, format=None):
#     if request.method == 'POST':

#         serializer = StockSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()

#             return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def fetchAllStock(request, format=None):
    if request.method == 'GET':

        #get all stock
        stock = Stock.objects.all()

        #serialize stock
        serializer = StockSerializer(stock, many=True)

        #return json
        return Response(serializer.data)


@api_view(['GET'])
def fetchStockForSpecificProduct(request, id, format=None):
    try:
        stock = Stock.objects.all().filter(product_id=id)
    except Stock.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method  == 'GET':
        serializer = StockSerializer(stock, many=True)
        return Response(serializer.data)