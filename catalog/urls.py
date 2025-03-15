from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import (
    ProductListView,
    ProductDetailView,
    ContactsTemplateView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductByCategoryListView,
    CategoryListView,
)

app_name = "catalog"
urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path(
        "product_detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"
    ),
    path("product_list/new/", ProductCreateView.as_view(), name="product_create"),
    path(
        "product_list/<int:pk>/update/",
        ProductUpdateView.as_view(),
        name="product_update",
    ),
    path(
        "product_list/<int:pk>/delete/",
        ProductDeleteView.as_view(),
        name="product_delete",
    ),
    path(
        "category/<int:category_id>/",
        ProductByCategoryListView.as_view(),
        name="product_category_list",
    ),
    path("category/", CategoryListView.as_view(), name="category_list"),
]
