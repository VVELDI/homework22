from django.urls import path
from .views import HomeView, ContactsView, CatalogView, ProductDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),  # Новый путь
]
