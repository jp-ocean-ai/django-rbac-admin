from rest_framework import permissions

from menutwo.models import Level1Model
from menutwo.serializer import Level1ModelSerializer
from utils.custom_viewset import CustomModelViewSet

class MenuTwoViewSet(CustomModelViewSet):
    queryset = Level1Model.objects.filter(is_delete=False)
    serializer_class = Level1ModelSerializer
    permission_classes = (permissions.IsAuthenticated,)
