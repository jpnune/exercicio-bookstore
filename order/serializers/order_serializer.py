# -*- coding: utf-8 -*-
from rest_framework import serializers

from product.models import Product
from product.serializers.product_serializer import ProductSerializer
from order.models import Order

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=True, many=True)
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()])
        return total

    class Meta:
        model = Order
        fields = ['product', 'total']
