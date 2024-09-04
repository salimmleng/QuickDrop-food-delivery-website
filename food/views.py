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



# class FoodItemsByCategoryAPIView(APIView):
#     def get(self, request, category_name=None):
#         if category_name == 'all':
#             food_items = FoodItem.objects.all()
#         else:
#             try:
#                 category = Category.objects.get(name=category_name)
#                 food_items = FoodItem.objects.filter(category=category)
#             except Category.DoesNotExist:
#                 return Response({'detail': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = FoodItemSerializer(food_items, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)



class FoodItemsByCategoryAPIView(APIView):
    def get(self, request, category_name=None, id=None):
        if id is not None:
            # Fetch the specific food item by ID
            try:
                food_item = FoodItem.objects.get(id=id)
                serializer = FoodItemSerializer(food_item)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except FoodItem.DoesNotExist:
                return Response({'detail': 'Food item not found'}, status=status.HTTP_404_NOT_FOUND)
        
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
    

    