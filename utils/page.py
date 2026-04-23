
from rest_framework.mixins import ListModelMixin
from rest_framework.pagination import PageNumberPagination


class PagenumCustomize(PageNumberPagination):
    page_query_param = 'p'
    page_size_query_param = 's'
    page_size = 5
    page_number = 3