from rest_framework import serializers
from .models import Category, FoodItem, Order, OrderItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class FoodItemSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = FoodItem
        fields = ['id', 'name', 'description', 'price', 'image']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['name', 'quantity', 'price']


class OrderSerializer(serializers.ModelSerializer):

    # orderitem = OrderItemSerializer(many=True)
    class Meta:

        model = Order
        fields = ['id', 'user', 'full_name', 'email', 'address', 'city', 'card_number', 'expiry_date', 'cvv', 'total_price', 'orderitem', 'created_at']

        read_only_fields = ["user",]

    # def create(self, validated_data):
    #     items_data = validated_data.pop('items')
    #     order = Order.objects.create(**validated_data)
    #     for item_data in items_data:
    #         OrderItem.objects.create(order=order, **item_data)
    #     return order
