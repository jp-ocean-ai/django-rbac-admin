from django.contrib import admin
# Register your models here.
from upload.models import UploadModel


class UploadAdmin(admin.ModelAdmin):
    # 新增和修改展示字段
    fields = ['image']
    # 列表展示字段
    list_display = ['id','image']

admin.site.register(UploadModel,UploadAdmin)