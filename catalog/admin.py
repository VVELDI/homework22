from django.contrib import admin

from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'image')  # Добавили image для отображения
    list_filter = ('category',)
    search_fields = ('name', 'description')

    # Чтобы изображение отображалось в форме редактирования
    fields = ('name', 'description', 'price', 'category', 'image')  # Убедимся, что поле image включено


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
