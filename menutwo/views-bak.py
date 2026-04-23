from django.shortcuts import render
# from rest_framework.generics import ListCreateAPIView
import requests

# Create your views here.
# from menus.models import FirstLevelMenu
# from menus.serializer import MenuSerializer
#
# class MenusGenericView(ListCreateAPIView):
#     serializer_class = MenuSerializer
#     queryset = FirstLevelMenu.objects.filter(is_delete=False)
from rest_framework import permissions

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from menus.models import FirstLevelMenu
from menutwo.models import Level1Model
from menutwo.serializer import Level1ModelSerializer

class MenuTwoViewSet(ModelViewSet):
    queryset = Level1Model.objects.filter(is_delete=False)
    serializer_class = Level1ModelSerializer
    # permission_classes = (permissions.IsAuthenticated,)

    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save() # 逻辑删除

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset,many=True)
        datas = serializer.data
        return Response(datas)

    def post(self, request, *args, **kwargs):
        pass