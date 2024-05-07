from django.db import models

# Create your models here.

class FoodOrder(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    pizza_quantity = models.IntegerField(default=0)
    burger_quantity = models.IntegerField(default=0)
    pasta_quantity = models.IntegerField(default=0)
    fries_quantity = models.IntegerField(default=0)
    cold_drinks_quantity = models.IntegerField(default=0)
    sandwich_quantity = models.IntegerField(default=0)
    dessert_quantity = models.IntegerField(default=0)
    dessert_choice = models.CharField(max_length=50, blank=True, null=True)
    delivery_location = models.CharField(max_length=200)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)


