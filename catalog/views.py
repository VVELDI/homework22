# catalog/views.py
from django.views.generic import ListView, TemplateView, DetailView
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product


# Главная страница
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


# Страница контактов
class ContactsView(View):
    template_name = 'contacts.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'success': False})

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        message = request.POST.get('message', '').strip()

        if name and phone and message:
            print(f"Получено сообщение от {name}, тел: {phone}: {message}")
            return render(request, self.template_name, {'success': True})
        else:
            # Вывод сообщения об ошибке (необязательно — зависит от шаблона)
            messages.error(request, "Пожалуйста, заполните все поля.")
            return render(request, self.template_name, {'success': False})


# Каталог товаров
class CatalogView(ListView):
    model = Product
    template_name = 'catalog.html'
    context_object_name = 'products'


# Детальная страница товара
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
