from django.urls import path
from .views import BudgetListCreateView

app_name = "budgets"

urlpatterns = [
    # /api/budgets/
    path('', BudgetListCreateView.as_view(), name='list-create'),
    # /api/budgets/5/
    # path('<int:pk>/', BudgetDetailView.as_view(), name='detail'),  # (optional for future)
]
