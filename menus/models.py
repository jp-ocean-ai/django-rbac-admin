from django.db import models

# Create your models here.
from utils.base_models import BaseModel

class FirstLevelMenu(BaseModel):
    # 之所以创建id是为了在接口文档中显示中文id主键，当存在primary_key时，不会再使用其它值当主键
    id = models.AutoField(verbose_name="id主键",primary_key=True,help_text="id主键")
    authname = models.CharField(verbose_name="一级菜单名称",max_length=10,help_text="一级菜单")
    path = models.CharField(verbose_name="一级菜单路径",max_length=10,help_text="一级菜单路径")
    # children = models.OneToOneField('menutwo.SecondLevelMenu',on_delete=models.CASCADE,help_text='对应二级菜单')

    class Meta:
        db_table = 'td_firstmenu'
        verbose_name = '一级菜单'
        verbose_name_plural = '一级菜单'

    def __str__(self):
        return self.authname