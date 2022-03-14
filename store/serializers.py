from unicodedata import category
from rest_framework import serializers
from .models import (
    Category_group, Category, Products, Sale_Products,
    Inventories
)

class CategorygroupSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Category_group
        fields = [
            'id', 'name', 'code'
        ]

class CategorySerailizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name', 'code', 'category_group'
        ]


# Category group model nested serializer 

class CategoryNested(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id', 'name', 'code', 'category_group'
        ]


class Category_relserializer(serializers.ModelSerializer):
    category_group = CategoryNested(many=True, read_only=True)

    class Meta:
        model = Category_group
        fields = ['id', 'name', 'code', 'category_group']




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




