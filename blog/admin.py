from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "preview", "is_published")
    list_filter = ("is_published",)
    search_fields = (
        "title",
        "is_published",
    )
