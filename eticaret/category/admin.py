from django.contrib import admin
from .models import Category
from .models import SubCategory

class SubCategoryInlineView(admin.TabularInline):
    model=SubCategory
    extra=5

class CategoryView(admin.ModelAdmin):
    list_display=["category_name","category_slug","category_image"]
    fields=["category_name","category_slug","category_image"]
    search_fields=["category_name","category_slug"]
    inlines=[SubCategoryInlineView]

class SubCategoryView(admin.ModelAdmin):
    list_display=["category_name","category_slug"]
    fields=["category_name","category_slug","parent_category"]


# Register your models here.
admin.site.register(Category,CategoryView)
admin.site.register(SubCategory,SubCategoryView)
