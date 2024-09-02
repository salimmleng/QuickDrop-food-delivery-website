from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, FoodItem
from .serializers import CategorySerializer, FoodItemSerializer

class CategoryListView(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class FoodItemsByCategoryAPIView(APIView):
    def get(self, request, category_name=None):
        if category_name == 'all':
            food_items = FoodItem.objects.all()
        else:
            try:
                category = Category.objects.get(name=category_name)
                food_items = FoodItem.objects.filter(category=category)
            except Category.DoesNotExist:
                return Response({'detail': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = FoodItemSerializer(food_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



