from django.contrib import admin
from .models import (
    Category_group, Category, Products, Sale_Products,
    Inventories
)

# Register your models here.
class Category_groupAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'category_group')

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity',
        'quantity_category', 'date_entered'
    )

class Sale_ProductsAdmin(admin.ModelAdmin):
    list_display = ('name','code', 'category', 'price',
        'quantity_category', 'date_entered'
    )

class InventoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity',
        'quantity_category', 'date_entered'
    )

admin.site.register(Category_group, Category_groupAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Sale_Products, Sale_ProductsAdmin)
admin.site.register(Inventories, InventoriesAdmin)