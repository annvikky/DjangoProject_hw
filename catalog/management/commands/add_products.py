from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Add test product to the database"

    def handle(self, *args, **options):
        # удаление данных перед загрузкой
        # Product.objects.all().delete()
        # Category.objects.all().delete()
        category, _ = Category.objects.get_or_create(
            name="Контейнер Пагода", description="Кондитерская упаковка"
        )

        products = [
            {
                "name": "Контейнер ПФК-35",
                "description": "Пищевая упаковка",
                "category": category,
                "price": 18,
            },
            {
                "name": "Контейнер ПФК-38",
                "description": "Пищевая упаковка",
                "category": category,
                "price": 27,
            },
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully added product: {product.name}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Product already exists: {product.name}")
                )
