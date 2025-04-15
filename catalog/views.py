from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views import View  # Импортируем базовый класс View
from django.views.generic import DetailView
from .models import Product



class HomeView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'home.html', {'products': products})


class ContactsView(View):
    """Контроллер страницы контактов"""

    def get(self, request):
        return render(request, 'contacts.html')

    def post(self, request):
        # Обработка формы (пример)
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Получено сообщение от {name}, тел: {phone}: {message}")
        return render(request, 'contacts.html', {'success': True})


class CatalogView(View):
    def get(self, request):
        return render(request, 'catalog.html')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
