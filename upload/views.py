from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.parsers import MultiPartParser, FormParser

from upload.models import UploadModel
from upload.serializer import UploadModelSerializer


# class UploadViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
#     queryset = UploadModel.objects.all()
#     serializer_class = UploadModelSerializer
#     parser_classes = (MultiPartParser, FormParser,)
from utils.custom_viewset import CustomModelViewSet


class UploadViewSet(CustomModelViewSet):
    queryset = UploadModel.objects.all()
    serializer_class = UploadModelSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_destroy(self, instance):
        instance.delete() # 硬删除-这里只是不在数据库存储，但是图片依然存在目录中
