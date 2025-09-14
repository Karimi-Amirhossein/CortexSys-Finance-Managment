"""
Main URL configuration for the finance_management project.
Includes admin routes and API endpoints for all apps.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # API endpoints
    path('api/transactions/', include('transactions.urls', namespace='transactions')),
    path('api/budgets/', include('budgets.urls', namespace='budgets')),
]
