from catalog.models import Product
from config.settings import CACHE_ENABLED
from django.core.cache import cache


def get_products_from_cache():
    """Получает список продуктов из кеша, при его отсутствии получает из БД."""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products, 60 * 15)
    return products


def get_products_from_category(category_id):
    """Получаем продукты по категории."""
    return Product.objects.filter(category_id=category_id)
