from django.db import models

from accounts.models import CustomerProfile
from stores.models import Product

# Create your models here.

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(CustomerProfile,on_delete=models.CASCADE)
    def __str__(self):
        return f"Cart {self.id} - {self.customer}"


class CartItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cart= models.ForeignKey(Cart,on_delete=models.CASCADE)
    def __str__(self):
        return f"CartItem {self.id} - {self.product.name}"


class Order(models.Model):
    customer = models.ForeignKey(CustomerProfile,on_delete=models.CASCADE)
    total_amount = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    default=0
) 
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Order {self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    price = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    default=0
) 
    quantity=models.IntegerField(default=1)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    def __str__(self):
        return f"OrderItem {self.id}-{self.product}"    