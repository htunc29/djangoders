from django.contrib import admin
from .models import Product
from .models import ProductImage
from .models import Tag
# Register your models here.
class ProductImageInlineView(admin.TabularInline):
    model=ProductImage
    extra=2


class ProductView(admin.ModelAdmin):
    list_display=["title","slug","price","category","description","is_active"]
    inlines=[ProductImageInlineView]



admin.site.register(Product,ProductView)
admin.site.register(ProductImage)
admin.site.register(Tag)


