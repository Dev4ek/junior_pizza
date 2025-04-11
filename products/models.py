from datetime import datetime
from django.db import models


class Users(models.Model):
    phone = models.TextField(max_length=20, unique=True)

class Products(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="products_images")
    
class Orders(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)
    