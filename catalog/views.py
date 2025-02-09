# from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView

from catalog.models import Product


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


# def home(request):
#     """Контроллер для отображения страницы home."""
#     return render(request, "catalog/home.html")


# def contacts(request):
#     """Контроллер для отображения страницы contacts."""
#     return render(request, "catalog/contacts.html")


# def products_list(request):
#     """Контроллер для отображения страницы с информацией о товарах."""
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, "catalog/product_list.html", context)


# def product_detail(request, pk):
#     """Контроллер для отображения страницы с информацией о товаре."""
#     product = get_object_or_404(Product, pk=pk)
#     context = {"product": product}
#     return render(request, "catalog/product_detail.html", context)
