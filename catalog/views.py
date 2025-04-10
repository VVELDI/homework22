from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def contacts(request):
    return render(request, 'contacts.html')

def catalog_home(request):  # Добавляем эту функцию
    return render(request, 'catalog.html')  # Убедитесь, что файл catalog.html существует