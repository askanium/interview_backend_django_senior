from rest_framework.pagination import LimitOffsetPagination


class SmallResultsSetPagination(LimitOffsetPagination):
    max_page_size = 1000
    default_limit = 3
