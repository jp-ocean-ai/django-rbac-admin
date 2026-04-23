from django.db import models

# Create your models here.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

from utils.base_models import BaseModel


class UploadModel(BaseModel):
    # name = models.CharField(verbose_name="上传图片名称",max_length=30,help_text="上传图片名称")
    image = models.ImageField(upload_to='upload',null=True,blank=True)

    class Meta:
        db_table = 'td_img'
        verbose_name = '图片列表'
        verbose_name_plural = verbose_name

# 硬删除操作
@receiver(pre_delete, sender=UploadModel)
def upload_model_delete(sender,instance,**kwargs):
    instance.image.delete(False)