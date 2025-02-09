from django.urls import path
from catalog.views import ProductListView, ProductDetailView, ContactsTemplateView

app_name = "catalog"
urlpatterns = [
    path("", ProductListView.as_view(), name="products_list"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path("product_detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
]
