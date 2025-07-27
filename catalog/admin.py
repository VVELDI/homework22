from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'status_display', 'owner_link', 'created_at')
    list_filter = ('status', 'category', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('category',)

    fields = (
        'name',
        'description',
        'price',
        'category',
        'image',
        'status',
        'owner',
        'created_at',
        'updated_at',
    )

    def status_display(self, obj):
        color = 'green' if obj.status == 'published' else 'red'
        label = '🟢 Опубликован' if obj.status == 'published' else '🔴 Черновик'
        return format_html(f'<strong style="color:{color}">{label}</strong>')

    status_display.short_description = 'Статус'
    status_display.admin_order_field = 'status'

    def owner_link(self, obj):
        if obj.owner:
            return format_html('<a href="/admin/users/customuser/{}/change/">{}</a>', obj.owner.id, obj.owner.email)
        return "-"
    owner_link.short_description = 'Владелец'
