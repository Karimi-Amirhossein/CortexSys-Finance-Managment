"""
Main URL configuration for the Finance_Management project.
Includes admin routes and API endpoints for all apps.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView)


urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # API endpoints
    path('api/transactions/', include('transactions.urls', namespace='transactions')),
    path('api/budgets/', include('budgets.urls', namespace='budgets')),
    path('api/accounts/', include('accounts.urls', namespace='accounts')),
    path('api/reports/', include('reports.urls', namespace='reports')),

    # API Authentication Endpoints
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # API Documentation Endpoints

    # Raw OpenAPI schema (JSON)
    path(
        "api/schema/",
        SpectacularAPIView.as_view(),
        name="api-schema"),

    # Interactive Swagger UI
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="swagger-ui"),

    # Alternative Redoc UI
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="api-schema"),
        name="redoc-ui"),
]
