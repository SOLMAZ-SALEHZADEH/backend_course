from django.db import models

from accounts.models import SellerProfile

# Create your models here.
class Store(models.Model):
    name= models.CharField(max_length=150)
    description= models.TextField(max_length=1000)
    owner=models.ForeignKey(SellerProfile, on_delete=models.CASCADE)
    balance = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    default=0
)
    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=110)
    price=models.DecimalField(max_digits=10,
        decimal_places=2,
        default=0)
    description=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='products-avatars/',blank=True,null=True)
    store=models.ForeignKey(Store, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    stock=models.IntegerField(default=0)
    def __str__(self):
        return self.name


