from django.shortcuts import render


def show_home(request):
    """" Контроллер для отображения страницы home."""
    return render(request, 'catalog/home.html')


def show_contacts(request):
    """" Контроллер для отображения страницы contacts."""
    return render(request, 'catalog/contacts.html')
