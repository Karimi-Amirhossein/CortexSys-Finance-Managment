"""
Main URL configuration for the finance_management project.
Includes admin routes and API endpoints for all apps.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # API endpoints
    path('api/transactions/', include('transactions.urls', namespace='transactions')),
    path('api/budgets/', include('budgets.urls', namespace='budgets')),
    path('api/accounts/', include('accounts.urls', namespace='accounts')),

    # API Authentication Endpoints
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
