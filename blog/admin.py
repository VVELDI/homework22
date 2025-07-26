from django.contrib import admin

from .forms import BlogForm  # ← подключаем форму с валидацией
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    form = BlogForm  # ← используем кастомную форму с цензурой
    list_display = ('title', 'created_at', 'is_published', 'views_count')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'content')
