# backend/serializers.py
from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    tags = serializers.StringRelatedField(many=True)
    class Meta:
        model = Item
        fields = ['user','sku', 'name', 'stock_status', 'available_stock', 'category', 'tags']
