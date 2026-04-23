

from rest_framework import serializers

from testaddress.models import TestAdressModel

class TestAddrModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestAdressModel
        fields = "__all__"