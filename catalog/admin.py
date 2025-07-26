from django.contrib import admin

from .forms import ProductForm  # ← подключаем форму с цензурой и проверкой цены
from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ProductAdmin(admin.ModelAdmin):
    form = ProductForm  # ← используем кастомную форму
    list_display = ('id', 'name', 'price', 'category', 'image')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    fields = ('name', 'description', 'price', 'category', 'image')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
