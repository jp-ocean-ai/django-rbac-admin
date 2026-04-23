
from rest_framework import routers

from menus.views import MenusViewSet
from menutwo.views import MenuTwoViewSet

rou = routers.DefaultRouter()

rou.register(prefix=r'menutwo',viewset=MenuTwoViewSet,basename='menutwo')
