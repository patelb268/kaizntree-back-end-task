from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        indexes = [
            models.Index(fields=['name'])
        ]

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name
    
    class Meta:
        indexes = [
            models.Index(fields=['name'])
        ]

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.user_name

class Item(models.Model):
    STOCK_STATUS_CHOICES = [
        ('low', 'Low'),
        ('empty', 'Empty'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, related_name='items')
    sku = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='items')
    stock_status = models.CharField(max_length=20, choices=STOCK_STATUS_CHOICES)
    available_stock = models.IntegerField()

    def __str__(self):
        return self.name
   