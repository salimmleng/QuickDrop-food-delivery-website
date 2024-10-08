from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, FoodItem,Order
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .serializers import CategorySerializer, FoodItemSerializer,OrderSerializer

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
    

    
    

class CheckoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        print(request.user)  # Debugging user info
        if serializer.is_valid():
            # Save the order and associate it with the authenticated user
            order = serializer.save(user=request.user)
            return Response({'success': True, 'order_id': order.id}, status=status.HTTP_201_CREATED)
        return Response({'success': False, 'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, order_id=None, user_id=None):
        if user_id:
            # Retrieve all orders for the specified user ID
            try:
                user = User.objects.get(id=user_id)
                orders = Order.objects.filter(user=user)
            except User.DoesNotExist:
                return Response({'success': False, 'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        elif order_id:
            # Retrieve a specific order by ID for the authenticated user
            try:
                order = Order.objects.get(id=order_id, user=request.user)
            except Order.DoesNotExist:
                return Response({'success': False, 'message': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

            # Serialize the specific order
            serializer = OrderSerializer(order)
            return Response({'success': True, 'order': serializer.data}, status=status.HTTP_200_OK)
        else:
            # Retrieve all orders for the authenticated user
            orders = Order.objects.filter(user=request.user)

        serializer = OrderSerializer(orders, many=True)
        return Response({'success': True, 'orders': serializer.data}, status=status.HTTP_200_OK)
