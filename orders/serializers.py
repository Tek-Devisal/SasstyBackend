from rest_framework import serializers

from orders.models import Ghanaian_Regions, DeliveryAddress, Orders

class GhanaianRegionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ghanaian_Regions
        fields = ['id', 'name']

class DeliveryAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAddress
        fields = ['id', 'user_id', 'is_primary', 'street_name', 'town', 'district', 'region']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['id', 'user_id', 'status', 'payment_status', 'order_code']

class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['id', 'order_code', 'delivery_address_id', 'product_id', 'quantity', 'prize', 'total_amount']
