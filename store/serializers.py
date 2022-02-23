from rest_framework import serializers
from .models import (
    Category_group, Category, Products, Sale_Products,
    Inventories
)

class CategorygroupSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Category_group
        fields = [
            'name', 'code'
        ]

class CategorySerailizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name', 'code', 'category_group'
        ]

class ProductSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = [
            'name', 'category', 'price', 'quantity',
            'quantity_category', 'date_entered'
        ]

class Sale_ProductSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Sale_Products
        fields = [
            'name', 'code', 'category', 'price',
            'quantity_category', 'date_entered'
        ]

class Sale_InventorySerailizer(serializers.ModelSerializer):
    class Meta:
        model = Inventories
        fields = [
            'name', 'category', 'price', 'quantity',
            'quantity_category', 'date_entered'
        ]




