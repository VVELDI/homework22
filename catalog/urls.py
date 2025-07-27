from django.urls import path

from .views import (
    HomeView, ContactsView, CatalogView,
    ProductDetailView, ProductCreateView, ProductUpdateView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Главная страница
    path('contacts/', ContactsView.as_view(), name='contacts'),  # Страница контактов
    path('catalog/', CatalogView.as_view(), name='catalog'),  # Страница каталога товаров
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),  # Страница одного товара
    path('product/create/', ProductCreateView.as_view(), name='product_create'),  # Создание товара
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),  # Редактирование
]
