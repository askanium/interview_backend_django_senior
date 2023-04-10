
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, OrderDeactivateUpdateView

urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('<int:id>/', OrderDeactivateUpdateView.as_view(), name='order-detail'),
    path('', OrderListCreateView.as_view(), name='order-list'),

]