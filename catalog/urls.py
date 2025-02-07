from django.urls import path
from catalog.views import contacts, products_list, product_detail


app_name = "catalog"
urlpatterns = [
    path("", products_list, name="products_list"),
    path("contacts/", contacts, name="contacts"),
    # path("products_list/", products_list, name="products_list"),
    path("product_detail/<int:pk>/", product_detail, name="product_detail"),
]
