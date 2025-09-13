from django.contrib import admin
from .models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    """Admin configuration for the Transaction model."""

    # Columns shown in the list view
    list_display = (
        "title",
        "user",
        "amount",
        "type",
        "category",
        "date",
        "created_at",
    )

    # Make fields clickable links (not only title)
    list_display_links = ("title", "user")

    # Sidebar filters
    list_filter = ("type", "category", "user", "date")

    # Enable search functionality
    search_fields = ("title", "category", "user__username", "user__email")

    # Default ordering
    ordering = ("-date", "-created_at")

    # Group fields in the edit form
    fieldsets = (
        ("Transaction Info", {"fields": ("title", "user", "amount", "type", "category")}),
        ("Additional Details", {"fields": ("date", "notes")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )

    # Make timestamps read-only
    readonly_fields = ("created_at", "updated_at")
