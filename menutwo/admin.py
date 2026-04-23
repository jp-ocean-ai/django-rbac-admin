from django.contrib import admin

from menutwo.models import Level1Model,Level2Model
# Register your models here.

class MenuLevel1Admin(admin.ModelAdmin):
    # 新增和修改展示字段
    fields = ['authname','path']
    # 列表展示字段
    list_display = ['id','authname','path']

class MenuLevel2Admin(admin.ModelAdmin):
    # 新增和修改展示字段
    fields = ['authname','path','level1']
    # 列表展示字段
    list_display = ['id','authname','path','level1_id']

admin.site.register(Level1Model,MenuLevel1Admin)
admin.site.register(Level2Model,MenuLevel2Admin)