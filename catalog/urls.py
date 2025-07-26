# catalog/urls.py
from django.urls import path
from .views import HomeView, ContactsView, CatalogView, ProductDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Главная страница
    path('contacts/', ContactsView.as_view(), name='contacts'),  # Страница контактов
    path('catalog/', CatalogView.as_view(), name='catalog'),  # Страница каталога товаров
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),  # Страница одного товара
]
