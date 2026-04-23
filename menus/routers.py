
from rest_framework import routers
from menus.views import MenusViewSet

route = routers.DefaultRouter()

route.register(prefix=r'menus',viewset=MenusViewSet,basename='menus')
