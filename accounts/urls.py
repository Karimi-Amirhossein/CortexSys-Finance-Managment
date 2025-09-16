from django.urls import path
from .views import RegisterView

# Namespace for accounts app URLs
app_name = "accounts"

urlpatterns = [
    # User registration endpoint (POST)
    path("register/", RegisterView.as_view(), name="register"),
]
