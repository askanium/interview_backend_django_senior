
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, OrderBetweenStartEmbargoListView

urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path(
        'between/<str:start>/<str:embargo>/',
        OrderBetweenStartEmbargoListView.as_view(),
        name='order-between-dates'),
    path('', OrderListCreateView.as_view(), name='order-list'),

]