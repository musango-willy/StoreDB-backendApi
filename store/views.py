from django.http import Http404
import json
# import pytz
from datetime import datetime, date, timedelta
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from django.utils import timezone

# from store import serializers
from .serializers import (
    CategorygroupSerailizer, CategorySerailizer, ProductSerailizer,
    Sale_ProductSerailizer, Sale_InventorySerailizer,Category_relserializer
)

# from store import models
from .models import (
    Category_group, Category, Products, Sale_Products,
    Inventories
)
from django.utils import timezone
# from django.utils.timezone import get_current_timezone



class CategoryGroupView(APIView):
    def get(self, request, format=None):
        groups = Category_group.objects.all()
        serializer = CategorygroupSerailizer(groups, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = self.add_post(data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def add_post(self, data):
        if isinstance(data, list):
            serializer = CategorygroupSerailizer(data=data, many=True)

            return serializer
        else:
            serializer = CategorygroupSerailizer(data=data)
            return serializer

# Category group + it relational models
@api_view(['GET'])
def category_relview(request):
        groups = Category_group.objects.all()
        serializer = Category_relserializer(groups, many=True)
        return Response(serializer.data)

class CategoryView(APIView):
    def get(self, request, format=None):
        category = Category.objects.all()
        serializer = CategorySerailizer(category, many=True)

        return Response(serializer.data)
     
    def post(self, request, format=None):
        data = request.data
        serializer = self.add_post(data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def add_post(self, data):
        if isinstance(data, list):
            serializer = CategorySerailizer(data=data, many=True)

            return serializer
        else:
            serializer = CategorySerailizer(data=data)
            return serializer

class ProductsView(APIView):
    def get_object(self,pk):
        try:
            return Products.object.get(pk=pk)
        except Products.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        category = Products.objects.all()
        serializer = ProductSerailizer(category, many=True)

        return Response(serializer.data)
     
    def post(self, request, format=None):
        serializer = ProductSerailizer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerailizer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Sale_ProductView(APIView):

    def get(self, request, format=None):
        sales_items = Sale_Products.objects.all()
        serializer = Sale_ProductSerailizer(sales_items, many=True)

        return Response(serializer.data)
     
    def post(self, request, format=None):
        rq = request.data
        if isinstance(rq, list):
            serializer = Sale_ProductSerailizer(data=request.data, many=True)

        else:
            serializer = Sale_ProductSerailizer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class InventoriesView(APIView):


     
    def post(self, request, format=None):
        data = request.data
        serializer = self.add_post(data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def add_post(self, data):
        if isinstance(data, list):
            serializer = Sale_InventorySerailizer(data=data, many=True)

            return serializer
        else:
            serializer = Sale_InventorySerailizer(data=data)
            return serializer


@api_view(['GET'])
def search_items(request, pk):
    try:
        int_ed = int(pk)
    except:
        int_ed = pk
    if request.method == "GET":
        item = Sale_Products.objects.filter(code__icontains=int_ed)|Sale_Products.objects.filter(name__icontains=pk)
        serializer = Sale_ProductSerailizer(item, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def inventoriesView(request):
    today = timezone.now().today()
    # yesterday = today - timedelta(days=7)
    obj = Inventories.objects.filter(date_entered__gte=today.date())

    df = pd.DataFrame.from_records(obj.values())

    data = df.resample('30T', on='date_entered').agg({'price':'sum', 'quantity':'sum'})
    data['time_data'] = data.index.tz_convert('Africa/Nairobi')

    data['time_data'] = data['time_data'].dt.strftime('%H:%M')

    data = data[data.price != 0]
    

    serializer = data.to_json(orient='records')
    parsed = json.loads(serializer)
    # print(data.head())
    return Response(parsed)