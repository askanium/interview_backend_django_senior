from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer


class OrderTagListView(APIView):
    model = Order
    serializer_class = OrderTagSerializer

    def get(self, request: Request, *args, **kwargs) -> Response:
        try:
            order = self.get_object(kwargs['id'])
        except Order.DoesNotExist:
            return Response(status=HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(order.tags.all(), many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def get_object(self, pk: int) -> Order:
        return self.model.objects.get(pk=pk)
