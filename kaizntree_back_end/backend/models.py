from django.db import models

# Create your models here.

class Item(models.Model):
    sku = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    tags = models.ManyToManyField('Tag')
    stock_status = models.CharField(max_length=50)
    available_stock = models.IntegerField()

class Tag(models.Model):
    name = models.CharField(max_length=50)