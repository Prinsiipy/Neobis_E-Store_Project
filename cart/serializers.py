from rest_framework import serializers
from decimal import Decimal

from .models import Cart, CartItem, Order


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = [
            'id',
            'quantity',
            'price',
            'product',
            'cart',
        ]


class CartSerializer(serializers.ModelSerializer):

    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = [
            'id',
            'user',
            'total_price',
            'created_date',
            'is_order',
        ]

    def get_total_price(self, obj):
        cart_id = obj.id
        cart_items = CartItem.objects.filter(cart=cart_id)
        total_price = 0

        for item in cart_items:
            if item.product.discount > 0:
                total_price += Decimal(item.price) - (Decimal(item.price) *
                                                 (Decimal(item.product.discount) / 100))
            else:
                total_price += Decimal(item.price)
        return total_price


class OrderSerializer(serializers.ModelSerializer):

    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'cart',
            'order_date',
            'total_price',
        ]

    def get_total_price(self,obj):
        cart_id = obj.cart.id
        cart_items = CartItem.objects.filter(cart=cart_id)
        total_price = 0

        for item in cart_items:
            if item.product.discount > 0:
                total_price += Decimal(item.price) - (Decimal(item.price) *
                                                      (Decimal(item.product.discount) / 100))
            else:
                total_price += Decimal(item.price)
        return total_price

