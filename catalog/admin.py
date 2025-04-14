from django.contrib import admin

from .models import Product, Category


# Настроим отображение для Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Показать id и name в списке


# Настроим отображение и фильтрацию для Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')  # Показать id, name, price, category
    list_filter = ('category',)  # Фильтрация по категории
    search_fields = ('name', 'description')  # Поиск по name и description


# Регистрация моделей в админке
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
