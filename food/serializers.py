
from rest_framework import serializers
from .models import Category, FoodItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class FoodItemSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = FoodItem
        fields = ['id', 'name', 'description', 'price', 'image']
