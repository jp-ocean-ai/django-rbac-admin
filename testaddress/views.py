from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from testaddress.models import TestAdressModel
from testaddress.serializer import TestAddrModelSerializer
from utils.custom_viewset import CustomModelViewSet, ReturnMsg
from utils.filter import AddrNameFilter


class ReturnMsgTotal:
    def __init__(self,msg='成功',errors=None,data=None,total=0,status=200):
        self.status = status
        self.msg = msg
        self.errors = {} if errors is None else errors
        self.data = [] if data is None else data
        self.total = total

    def dict(self):
        return {
            'data': self.data,
            'total': self.total,
            'meta': {
                'msg': self.msg,
                'errors': self.errors,
                'status': self.status
            }
        }


class MyPage(PageNumberPagination):
    #  指定控制每页数量的参数，前端发送的每页数目关键字
    page_size_query_param = 'pagesize'
    #  前端发送页数关键字
    page_query_param = 'pagenum'
    # 每页数目
    # page_size =
    # 指定每页最大返回数量
    max_page_size = 10000


class TestAddrViewSet(CustomModelViewSet):
    queryset = TestAdressModel.objects.filter(is_delete=False).order_by("create_time")
    # 分页
    pagination_class = MyPage
    # 展示序列化器
    serializer_class = TestAddrModelSerializer
    # 过滤引擎
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    # 指定过滤器类
    filter_class = AddrNameFilter
    # 指定过滤字段
    # filterset_fields = ['addrname']
    # 搜索
    search_fields = ('query')
    # 指定排序字段
    ordering_fields = ['create_time']


    # def list(self, request, *args, **kwargs):
    #     total = TestAdressModel.objects.filter(is_delete=False).count()
    #     response = super().list(request, *args, **kwargs)
    #     return Response(ReturnMsgTotal(data=response.data, status=response.status_code,total=total).dict(), status=response.status_code)
