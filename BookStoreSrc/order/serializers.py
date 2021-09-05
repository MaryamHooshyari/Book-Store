from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    book = serializers.RelatedField(source='book', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['book.title', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    owner = serializers.RelatedField(source='owner', read_only=True)
    address = serializers.RelatedField(source='address', read_only=True)

    class Meta:
        model = Order
        fields = ['owner.email', 'address', 'discount_code', 'items']
