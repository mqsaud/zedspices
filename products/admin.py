from django.contrib import admin
from .models import Product, Category, RateAndReview

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        
        'name',
        'friendly_name',
    )

    ordering = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'credit',
    )

    ordering = ('sku',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(RateAndReview)
