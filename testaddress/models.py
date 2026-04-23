from django.db import models

# Create your models here.
from django.db import models
from utils.base_models import BaseModel

class TestAdressModel(BaseModel):
    addrname = models.CharField(verbose_name="测试地址名称",max_length=10,help_text="测试地址名称")
    uataddr = models.CharField(verbose_name="uat地址url",max_length=200,help_text="uat地址url")
    prodaddr = models.CharField(verbose_name="prod地址url",max_length=200,help_text="prod地址url")

    class Meta:
        db_table = 'td_addr'
        verbose_name = "测试地址"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.addrname