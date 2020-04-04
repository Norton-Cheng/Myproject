from django.db import models

# Create your models here.

class Message(models.Model):
    # 姓名
    pname=models.CharField(max_length=20)
    # 手机
    pphone=models.CharField(max_length=11,default='')
    # 邮箱
    pemail=models.CharField(max_length=50)
    # 地址
    padderss=models.CharField(max_length=100,default='')
    # 备注
    pbeizhu=models.CharField(max_length=200,default='')
    # 逻辑删除
    isDelete=models.BooleanField(default=False)
    # 元选项
    class Meta:
        db_table='message'

class Product(models.Model):
    # 产品名
    ptitle=models.CharField(max_length=20)
    # 产品图片
    ppicture=models.CharField(max_length=20)
    # 产品介绍
    pintro=models.CharField(max_length=200)
    # 产品详情
    pcontent=models.CharField(max_length=400)
    # 元选项
    class Meta:
        db_table='product'