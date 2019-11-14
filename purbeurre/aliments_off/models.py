from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Products(models.Model):
    id_product = models.IntegerField()
    product_name = models.CharField(max_length=200)
    nutritional_score = models.CharField(max_length=2)
    url = models.URLField()
    category_name = models.CharField(max_length=200)
    img_url = models.URLField()
    fat = models.CharField(max_length=8, null=True)
    fat_100g = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    saturated_fat = models.CharField(max_length=8, null=True)
    saturated_fat_100g = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    sugars = models.CharField(max_length=8, null=True)
    sugars_100g = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    salt = models.CharField(max_length=8, null=True)
    salt_100g = models.DecimalField(max_digits=3, decimal_places=1, null=True)

    def __str__(self):
        return self.product_name

class SaveProducts(models.Model):
    id_product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)