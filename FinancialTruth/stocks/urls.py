from django.urls import path
from . import views

urlpatterns = [
    path('', views.StockView.as_view()),
    path('<slug:slug>/', views.StockDetailView.as_view(), name='stocks_detail')
]