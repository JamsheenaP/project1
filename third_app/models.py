from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField()
    category = models.CharField(max_length=50)
    description = models.TextField()
