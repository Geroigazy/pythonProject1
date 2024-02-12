import uuid
from django.contrib.auth import get_user_model
from django.db import models




class Category(models.Model):
    name = models.CharField(max_length=30)


class Product(models.Model):
    name = models.CharField(max_length=30, null=False)
    price = models.FloatField(default=0, null=False)
    description = models.TextField()
    quantity = models.IntegerField(default=0, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    is_active = models.BooleanField(default=True)



