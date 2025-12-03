from django.db import models

# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=50)
    category_slug=models.SlugField(unique=True,blank=False)
    category_image=models.ImageField(upload_to="kategori_resimleri")
    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    category_name=models.CharField(max_length=50)
    category_slug=models.SlugField(unique=True,blank=False)
    parent_category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="altkategoriler")
    def __str__(self):
        return self.category_name

