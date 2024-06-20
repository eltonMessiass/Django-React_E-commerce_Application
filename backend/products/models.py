from django.db import models
from categories.models import Category
# Create your models here.



class Product(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    stock = models.IntegerField()


    def __str__(self):
        return self.name
