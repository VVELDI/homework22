from django.views.generic import ListView, TemplateView, DetailView
from django.views import View
from django.shortcuts import render
from .models import Product


class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'


class ContactsView(TemplateView):
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = False
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Получено сообщение от {name}, тел: {phone}: {message}")
        return render(request, self.template_name, {'success': True})


class CatalogView(ListView):
    model = Product
    template_name = 'catalog.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
