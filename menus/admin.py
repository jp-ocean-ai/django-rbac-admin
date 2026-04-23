from django.contrib import admin

from menus.models import FirstLevelMenu
# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    # 新增和修改展示字段
    fields = ['authname','path']
    # 列表展示字段
    list_display = ['authname','path']

admin.site.register(FirstLevelMenu,MenuAdmin)
