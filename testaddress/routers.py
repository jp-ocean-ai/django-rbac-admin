
from rest_framework import routers

from testaddress.views import TestAddrViewSet

rou_testaddress = routers.DefaultRouter()

rou_testaddress.register(prefix=r'AlipayAddr',viewset=TestAddrViewSet,basename='AlipayAddr')
