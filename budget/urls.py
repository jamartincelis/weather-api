from django.urls import path
from . import views

app_name = "budget"
urlpatterns = [
    path('',views.budget_list),
    path('<str:pk>/', views.BudgetDetail.as_view()),
]