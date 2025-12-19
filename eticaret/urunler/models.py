from django.db import models
# from category.models import Category
from category import models as category_model
# slugify için kütüphanesi için
from django.utils.text import slugify
#unique id
import uuid

class Tag(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(unique=True,blank=False)
    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        if not self.slug:
            unique=uuid.uuid4().hex[:8]
            link=slugify(self.title)
            self.slug=f"{link}-{unique}"
        super().save(*args,**kwargs)


class Product(models.Model):
    title=models.CharField(max_length=200)
    short_description=models.CharField(max_length=220)
    description=models.TextField(max_length=500)

    slug=models.SlugField(unique=True,blank=True)

    price=models.DecimalField(max_digits=10,decimal_places=2)
    discount_price=models.DecimalField(max_digits=10,decimal_places=2,blank=True)
    is_active=models.BooleanField(default=True)
    stock=models.PositiveIntegerField(default=0)
    category=models.ForeignKey(category_model.Category,on_delete=models.PROTECT,related_name="products")
    tags=models.ManyToManyField(Tag)
    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        if not self.slug:
            unique=uuid.uuid4().hex[:8]
            link=slugify(self.title)
            self.slug=f"{link}-{unique}"
        super().save(*args,**kwargs)
    def discount_percent(self):
        return int((self.price-self.discount_price)*100/self.price)
    def fulltitle(self):
        return f"{self.title}-{self.slug}"
class ProductImage(models.Model):
    image=models.ImageField(upload_to="product_images")
    alt_text=models.CharField(max_length=200)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="images")
    is_main=models.BooleanField(default=False)


