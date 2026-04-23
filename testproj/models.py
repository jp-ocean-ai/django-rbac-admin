from django.db import models
from utils.base_models import BaseModel

# Create your models here.


class TestProjectModel(BaseModel):
    projectname = models.CharField(verbose_name="项目名称",max_length=200,help_text="项目名称")
    casenum = models.CharField(verbose_name="用例数", max_length=200, help_text="用例数")
    bugnum = models.CharField(verbose_name="bug数", max_length=200, help_text="bug数")
    autotestnum = models.CharField(verbose_name="自动化数目", max_length=200, help_text="自动化数目")

    class Meta:
        db_table = 'td_pjname'
        verbose_name = "项目名称"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.projectname
