
from rest_framework import serializers
from menus.models import FirstLevelMenu

class MenuModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstLevelMenu
        exclude = ('create_time','update_time','is_delete')

