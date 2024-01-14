from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)


class Product(models.Model):
    name = models.CharField(max_length=30, null=False)
    price = models.FloatField(default=0, null=False)
    description = models.TextField()
    quantity = models.IntegerField(default=0, null=False)
    category_id = models.ForeignKey(Category, on_delete = models.CASCADE)
    is_active = models.BooleanField(default=False)
