from rest_framework import serializers

from cart.models import Cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'product_id', 'user_id', 'quantity', 'prize', 'total_amount']
