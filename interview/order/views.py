# standard library
import datetime

# third party
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

# local Django
from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer


# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderBetweenStartEmbargoListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except ValueError:
            return Response(
                "Invalid `start_date` or `embargo_date` format. Should be YYYY-MM-DD",
                status=HTTP_400_BAD_REQUEST
            )

    def validate_query_params(self):
        try:
            datetime.date.fromisoformat(self.kwargs.get('start', ''))
            datetime.date.fromisoformat(self.kwargs.get('embargo', ''))
        except ValueError:
            raise ValueError("Incorrect date format, should be YYYY-MM-DD")

    def filter_queryset(self, queryset):
        self.validate_query_params()
        start_date = self.kwargs.get('start')
        embargo_date = self.kwargs.get('embargo')
        queryset = self.get_queryset()

        return queryset.filter(start_date__gte=start_date, embargo_date__lte=embargo_date)


class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer
