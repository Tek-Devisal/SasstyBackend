from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from cart.models import Cart
from cart.serializers import CartSerializer
from orders.models import DeliveryAddress, OrderProducts, Orders

from orders.serializers import DeliveryAddressSerializer, OrderProductSerializer, OrderSerializer
from rest_framework import status

@api_view(['POST'])
def addDeliveryAddress(request, format=None):
    if request.method == 'POST':

        serializer = DeliveryAddressSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def updateDeliveryAddress(request, id, format=None):
    if request.method == 'PUT':
        item_to_edit = DeliveryAddress.objects.all().filter(pk=id)
        serializer = DeliveryAddressSerializer(instance= item_to_edit, data=request.data)

        if serializer.is_valid():
            serializer.update()

            return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['DELETE'])
def removeDeliveryAddress(request, id, format=None):
    if request.method == 'DELETE':
        item_to_remove = DeliveryAddress.objects.all().filter(pk=id)
        serializer = DeliveryAddressSerializer(instance= item_to_remove, data=request.data)

        if serializer.is_valid():
            item_to_remove.delete()

            return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def fetchAllDeliveryAddressesPerUser(request, user_id, format=None):
        try:
            address = DeliveryAddress.objects.all().filter(user_id=user_id, is_primary = True)
        except DeliveryAddress.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method  == 'GET':
            serializer = DeliveryAddressSerializer(address, many=True)
            return Response(serializer.data)


@api_view(['PUT'])
def setDeliveryAddressAsPrimary(request, address_id):
    if request.method == 'PUT':
            address = DeliveryAddress.objects.all().filter(pk=address_id)
            serializer = DeliveryAddressSerializer(instance=address, data=request.data)

            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)

# ORDERd
@api_view(['POST'])
def addNewOrder(request, user_id):
    #MOVE ITEM FROM CART TO ORDERS
    #CHECK IF THERE IS A CURRENT ORDER IN SESSION
    if request.method == 'POST':
        try:
            orders = Orders.objects.all().filter(user_id = user_id, status = 0)
        except Orders.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = OrderSerializer(orders.first())
        the_order =  serializer.data['order_code']
        if the_order != "":
            #LOOP THROUGH THE CART AND SAVE IN ORDER PRODUCTS
            try:
                cart_items = Cart.objects.all().filter(user_id = user_id)
            except Cart.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
            serializer = CartSerializer(cart_items, many=True)
            length_cart_items = len(serializer.data)
            for _ in range (0, length_cart_items):
                #ADD CART ITEMS TO ORDERS
                # OrderProducts.objects.create(order_code = the_order, delivery_address_id = request.data['delivery_address_id'],product_id = serializer.data['product_id'], user_id = serializer.data['user_id'], quantity = serializer.data['quantity'], prize = serializer.data['prize'], total_amount = serializer.data['total_amount'])
                # a.append(serializer.data['product_id'])
                # order_products_serializer =  OrderProductSerializer(data=serializer.data)

                # if order_products_serializer.is_valid():
                #     order_products_serializer.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            serializer = OrderSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                addNewOrder(request, user_id)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        #THERE IS NO ORDER
        
        # if(the_order == ""):
        #      #ADD NEW ORDER
        #     serializer = OrderSerializer(data=request.data)
        #     if serializer.is_valid():
        #         serializer.save()
        #         return Response(serializer.data, status=status.HTTP_201_CREATED)
        # #THERE IS AN ORDER
        # else:
        #     return "aN ORDER IS HERE"
        #IF NOT ADD NEW ORDER
        #OTHERWISE ADD THE ORDER ITEMS
        # serializer = OrderSerializer(data=request.data)

        # if serializer.is_valid():
        #     serializer.save()

        #     return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def fetchAllOrders(request):
    try:
        orders = Orders.objects.all()
    except Orders.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method  == 'GET':
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
        # return Response([{"order":serializer.data[0]['status'], "user":{"id": "45432343-AAA"}}])
