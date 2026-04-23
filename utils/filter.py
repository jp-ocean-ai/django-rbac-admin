from django_filters import rest_framework as filters

from testaddress.models import TestAdressModel
from testproj.models import TestProjectModel


class AddrNameFilter(filters.FilterSet):
    query = filters.CharFilter(field_name="addrname",lookup_expr="icontains")

    class Meta:
        model = TestAdressModel
        fields = ['addrname']


class TestProjectFilter(filters.FilterSet):
    query = filters.CharFilter(field_name="projectname",lookup_expr="icontains")

    class Meta:
        model = TestProjectModel
        fields = ['projectname']