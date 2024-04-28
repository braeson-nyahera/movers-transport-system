from django.urls import path
from transportation import views
from .views import OrderListView

urlpatterns = [
    path('orders/',OrderListView.as_view(), name='orders_list'),
]