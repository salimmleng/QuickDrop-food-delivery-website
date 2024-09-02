from django.urls import path
from .views import CategoryListView, FoodItemsByCategoryAPIView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('food-items/<str:category_name>/', FoodItemsByCategoryAPIView.as_view(), name='food-items-by-category'),
]
