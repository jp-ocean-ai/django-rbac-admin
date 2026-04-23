
from rest_framework import routers

from testproj.views import TestProjectViewSet

roucc = routers.DefaultRouter()

roucc.register(prefix=r'testproj',viewset=TestProjectViewSet,basename='testproj')
