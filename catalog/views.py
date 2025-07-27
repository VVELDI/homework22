from django.views.generic import (
    ListView, TemplateView, DetailView,
    CreateView, UpdateView
)
from django.views import View
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin  # 👈 добавили

from .models import Product
from .forms import ProductForm


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


# Создание продукта — только для авторизованных
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('home')


# Редактирование продукта — только для авторизованных
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('home')
