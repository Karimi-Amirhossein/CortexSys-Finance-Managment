from django.urls import path
from .views import TransactionListCreateView, TransactionDetailView

# By setting app_name, we create a namespace for our app's URLs.
# This is a best practice to avoid URL name collisions with other apps.
app_name = "transactions"

urlpatterns = [
    # Maps the root URL of this app (e.g., /api/transactions/) to our view.
    path('', TransactionListCreateView.as_view(), name='list-create'), 
    path('<int:pk>/', TransactionDetailView.as_view(), name='detail'),
]
