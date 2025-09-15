from django.urls import path
from .views import BudgetListCreateView, BudgetDetailView

app_name = "budgets"

urlpatterns = [
    # /api/budgets/
    path('', BudgetListCreateView.as_view(), name='list-create'),
    path('<int:pk>/', BudgetDetailView.as_view(), name='detail'),
]
