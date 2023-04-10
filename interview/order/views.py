from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer


class OrderDeactivateUpdateView(APIView):
    """
    Deactivate an order by setting is_active to False.

    In theory, we don't send any data with the PATCH request to update
    the instance with, therefore a POST would work here as well. However,
    I have used PATCH to indicate that only a subset of instance data is
    affected.
    """
    def patch(self, request, *args, **kwargs):
        should_deactivate = request.query_params.get('deactivate') == 'true'
        # NOTE: the class method does not return anything (because it uses
        # .filter(), which can return empty queryset) so we cannot tell the
        # user whether they have provided a proper instance ID.
        if should_deactivate:
            Order.deactivate(kwargs["id"])
        return Response(status=HTTP_200_OK)
