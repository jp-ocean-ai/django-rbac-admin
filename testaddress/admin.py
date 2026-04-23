from django.contrib import admin
# Register your models here.
from testaddress.models import TestAdressModel

class TestAdressAdmin(admin.ModelAdmin):
    # 新增和修改展示字段
    fields = ['addrname','uataddr','prodaddr']
    # 列表展示字段
    list_display = ['id','addrname','uataddr','prodaddr']

admin.site.register(TestAdressModel,TestAdressAdmin)