
from rest_framework import serializers

from menutwo.models import Level2Model, Level1Model


# 二级目录序列化器
class Level2ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level2Model
        # fields = ['id','authname','path','level']
        # fields = "__all__"
        fields = ['id','authname','path','level1']

# 一级目录序列化器
class Level1ModelSerializer(serializers.ModelSerializer):
    # related_name名称
    children = Level2ModelSerializer(many=True)
    class Meta:
        model = Level1Model
        fields = ['id','authname','path','children']