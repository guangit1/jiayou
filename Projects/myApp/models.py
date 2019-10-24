from django.db import models

# Create your models here.

class Grades(models.Model):   ##继承models的Model
    gname = models.CharField(max_length=20)  #字段的类型第一个都是大写的
    gdate = models.DateTimeField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField() ## 还有一个是NullBooleanField(),None/True/False


class Students(models.Model):
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True) ##设置默认值，default=True/False
    sage = models.IntegerField()
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    sgrade = models.ForeignKey("Grades")  ## 关联外键，一对多，写在多的里面
## 说明：不需要定义主键，在生成时自动添加，并且值为自动增加
### 注：一个类对应数据库中的一个表，类里面的属性会对应表里面的一个字段。