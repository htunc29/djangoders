from django.contrib import admin
from .models import Product
from .models import ProductImage
from .models import Tag
# Register your models here.
class ProductImageInlineView(admin.TabularInline):
    model=ProductImage
    extra=12


class ProductView(admin.ModelAdmin):
    list_display=["title","slug","price","discount_price","discount_percent","fulltitle","category","description","is_active","created_at","updated_at"]
    inlines=[ProductImageInlineView]



admin.site.register(Product,ProductView)
admin.site.register(ProductImage)
admin.site.register(Tag)


