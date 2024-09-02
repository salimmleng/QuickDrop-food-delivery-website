from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class FoodItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='food_items')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='food/food_images/')

    def __str__(self):
        return self.name