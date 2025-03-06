from django.urls import path
from catalog.views import ProductListView, ProductDetailView, ContactsTemplateView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView

app_name = "catalog"
urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path("product_detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product_list/new/", ProductCreateView.as_view(), name="product_create"),
    path("product_list/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("product_list/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
]
