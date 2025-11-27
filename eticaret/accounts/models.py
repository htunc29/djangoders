from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=50)
    slug=models.SlugField(unique=True,blank=False)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name=models.CharField(max_length=100)
    stock=models.IntegerField()
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField(max_length=500)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")
    slug=models.SlugField(unique=True,blank=False)
    def __str__(self):
        return self.product_name
