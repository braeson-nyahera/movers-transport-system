from django.urls import path
from transportation import views
from .views import OrderListView, OrderDetailView

urlpatterns = [
    path('orders/',OrderListView.as_view(), name='orders_list'),
    path('orders/<pk>',OrderDetailView.as_view(), name='order-detail'),
]