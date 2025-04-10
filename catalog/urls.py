from django.urls import path
from .views import HomeView, ContactsView, CatalogView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('catalog/', CatalogView.as_view(), name='catalog'),  # Новый путь
]