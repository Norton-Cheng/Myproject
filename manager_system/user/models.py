from django.db import models

# user app:用来管理注册、登录
'''
Userinfo
属性：账号、密码
'''
class Userinfo(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=100)
    class Meta:
        db_table='userinfo'
