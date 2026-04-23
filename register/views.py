from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.

# 只有一个请求post方法
# 那个视图中提供post方法

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from register.serializer import RegisterModelSerializer

'''
继承GenericAPIView时，需指定query_set和serializer_class
'''

class RegisterView(CreateAPIView):
    # 获取项目列表时，要query_set
    # 获取详情 query_set,
    # queryset = User.objects.all
    serializer_class = RegisterModelSerializer
    # authentication_classes = (JSONWebTokenls
    # Authentication,)