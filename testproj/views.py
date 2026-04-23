from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination

from testproj.models import TestProjectModel
from testproj.serializer import TestProjectSerializer
from utils.custom_viewset import CustomModelViewSet
from utils.filter import TestProjectFilter
from rest_framework.viewsets import ModelViewSet


class MyPage(PageNumberPagination):
    #  指定控制每页数量的参数，前端发送的每页数目关键字
    page_size_query_param = 'pagesize'
    #  前端发送页数关键字
    page_query_param = 'pagenum'
    # 每页数目
    # page_size = 5
    # 指定每页最大返回数量
    max_page_size = 10000


# class TestProjectViewSet(ModelViewSet):
#     queryset = TestProjectModel.objects.filter(is_delete=False)
#     # 分页
#     pagination_class = MyPage
#     serializer_class = TestProjectSerializer
#     # 权限
#     # permission_classes = (permissions.IsAuthenticated,)
#     # 过滤引擎
#     # filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
#     # 过滤
#     filter_class = TestProjectFilter
#     # 搜索
#     search_fields = ('query')
    # 排序
    # ordering_fields = ['create_time']


class TestProjectViewSet(CustomModelViewSet):
    # 权限
    permission_classes = (permissions.IsAuthenticated,)

    queryset = TestProjectModel.objects.filter(is_delete=False)
    # 分页
    pagination_class = MyPage
    serializer_class = TestProjectSerializer

    # 过滤引擎
    # filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # 过滤
    filter_class = TestProjectFilter
    # 搜索
    search_fields = ('query')
    # 排序
    # ordering_fields = ['create_time']