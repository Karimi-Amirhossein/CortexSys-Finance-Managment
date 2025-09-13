from django.contrib import admin
from .models import Budget


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    """Admin configuration for the Budget model."""

    # Columns shown in the list view
    list_display = (
        "title",
        "user",
        "total_amount",
        "start_date",
        "end_date",
        "category",
        "created_at",
    )

    # Make some fields clickable links (instead of only the title)
    list_display_links = ("title", "user")

    # Add filters in the sidebar
    list_filter = ("user", "category", "start_date", "end_date")

    # Add search functionality
    search_fields = ("title", "category", "user__username", "user__email")

    # Default ordering
    ordering = ("-end_date", "-created_at")

    # Show fields in the form view (organized by sections)
    fieldsets = (
        ("Budget Info", {"fields": ("title", "user", "category")}),
        ("Period & Amount", {"fields": ("total_amount", "start_date", "end_date")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )

    # Read-only fields for timestamps
    readonly_fields = ("created_at", "updated_at")
