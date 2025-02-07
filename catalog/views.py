from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    """Контроллер для отображения страницы home."""
    return render(request, "catalog/home.html")


def contacts(request):
    """Контроллер для отображения страницы contacts."""
    return render(request, "catalog/contacts.html")


def products_list(request):
    """Контроллер для отображения страницы с информацией о товарах."""
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "catalog/products_list.html", context)


def product_detail(request, pk):
    """Контроллер для отображения страницы с информацией о товаре."""
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "catalog/product_detail.html", context)
