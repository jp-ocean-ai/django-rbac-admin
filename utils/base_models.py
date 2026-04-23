from django.db import models

class BaseModel(models.Model):
    # 数据库公共字段
    # auto_now_add 当创建数据的时候创建一个时间，以后就不会改了，相当于注册时间
    # auto_now 相当于最后登录时间，一旦修改数据自动会更新时间
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间",help_text="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间", help_text="更新时间")
    is_delete = models.BooleanField(default=False,verbose_name="逻辑删除",help_text="逻辑删除")

    class Meta:
        # 设置为抽象模型类时，当数据库迁移时不会创建数据库，供其他类继承使用
        abstract = True
        verbose_name = "公共表字段"
        # db_table = "BaseModel"