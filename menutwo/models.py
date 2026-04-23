from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from utils.base_models import BaseModel

class Level1Model(BaseModel):
    id = models.BigAutoField(primary_key=True,verbose_name="一级菜单id")
    authname = models.CharField(max_length=15,verbose_name="一级菜单名称",help_text="一级菜单名称")
    path = models.CharField(max_length=15,verbose_name="一级菜单路径",help_text="一级菜单路径")

    class Meta:
        db_table = 'td_menu_lv1'
        verbose_name = "一级菜单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.authname

class Level2Model(BaseModel):
    id = models.BigAutoField(primary_key=True,verbose_name="二级菜单id")
    authname = models.CharField(max_length=15,verbose_name="二级菜单名称",help_text="二级菜单名称")
    path = models.CharField(max_length=15,verbose_name="二级菜单路径",help_text="二级菜单路径")

    level1 = models.ForeignKey(Level1Model,on_delete=models.CASCADE,verbose_name="一级菜单id外键",
                               related_name='children',null=True)

    class Meta:
        db_table = 'td_menu_lv2'
        verbose_name = "二级菜单"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.authname