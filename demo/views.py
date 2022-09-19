from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from demo.models import Product, Shop
from demo.serializers import ProductSerializer


class ProductView(APIView):
    def get(self, request, *args, **kwargs):
        shop = Shop.objects.create(name='Svyazonoy', state=True)
        Product.objects.create(price=100000, quantity=10, category='phones', name='iphone', shop=shop)
        queryset = Product.objects.all().select_related('shop')
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.save()
            return Response(ProductSerializer(product).data)
        else:
            return Response(serializer.errors)
