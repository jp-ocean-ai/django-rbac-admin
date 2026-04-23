

from rest_framework import serializers

from testproj.models import TestProjectModel


class TestProjectSerializer(serializers.ModelSerializer):
    # create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = TestProjectModel
        fields = "__all__"