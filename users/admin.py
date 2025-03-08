from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "password", "phone_number", "avatar")
    list_filter = ("email",)
    search_fields = ("email",)
