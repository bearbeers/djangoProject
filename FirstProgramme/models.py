import time

from django.db import models

# Create your models here.
class UserInfo(models.Model):
    email = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()
    birth = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    remark = models.CharField(null=True, blank=True, max_length=128)


# UserInfo.objects.create(name=) 增加数据
# UserInfo.objects.filter(id=).delete()  删除数据
# UserInfo.objects.all().delete()  删除表中所有数据
# UserInfo.objects.all()  获取表中所有数据
# UserInfo.objects.filter(id=1).first()  获取符合条件的数据的中第一条
# UserInfo.objects.filter(id=).update(age=)
# UserInfo.objects.all().update()
