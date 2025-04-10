from django.shortcuts import render
from django.views import View  # Импортируем базовый класс View


class HomeView(View):
    """Контроллер главной страницы"""

    def get(self, request):
        return render(request, 'home.html')


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
