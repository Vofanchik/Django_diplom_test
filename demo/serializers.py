from rest_framework import serializers
from demo.models import Shop
from demo.models import Product

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name', 'state',]

class ProductSerializer(serializers.ModelSerializer):
    # shop = serializers.StringRelatedField()
    shop = ShopSerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'quantity', 'price', 'shop',]