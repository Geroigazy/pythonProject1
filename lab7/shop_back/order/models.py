import uuid

from django.db import models
from api.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')
    created_at = models.DateTimeField(auto_now_add=True)
