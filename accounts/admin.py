from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Custom admin panel for the CustomUser model."""

    # Add the custom "is_verified" field to the default UserAdmin fieldsets
    fieldsets = UserAdmin.fieldsets + (
        ("Extra Information", {"fields": ("is_verified",)}),
    )

    # Add the "is_verified" field to the form for creating new users
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("is_verified",)}),
    )

    # Columns displayed in the user list view
    list_display = ("username", "email", "is_staff", "is_active", "is_verified")

    # Enable search functionality for username and email
    search_fields = ("username", "email")

    # Add filters in the sidebar for quick filtering
    list_filter = ("is_staff", "is_active", "is_verified")
