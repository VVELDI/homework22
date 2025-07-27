from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, TemplateView, DetailView,
    CreateView, UpdateView, DeleteView
)
from django.views import View
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm


# Главная страница
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(status='published')
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

    def get_queryset(self):
        return Product.objects.filter(status='published')


# Детальная страница товара
class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


# Создание продукта
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


# Редактирование продукта
class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        product = self.get_object()
        return product.owner == self.request.user


# Удаление продукта (доступно владельцу или модератору)
class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        product = self.get_object()
        user = self.request.user
        return product.owner == user or user.has_perm('catalog.can_unpublish_product')
