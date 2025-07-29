from django.urls import path
from .views import (
    HomeView, ContactsView, CatalogView, ProductDetailView,
    ProductCreateView, ProductUpdateView, ProductDeleteView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]
