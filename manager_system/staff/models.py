from django.db import models

# Create your models here.
class Staffinfo(models.Model):
    name=models.CharField(max_length=20,default='')
    birthday=models.DateField(default='')
    # True代表男 False代表女
    gender=models.BooleanField(default=True)
    phone=models.CharField(max_length=11,default='')
    salary=models.DecimalField(max_digits=8,decimal_places=2,default=2480)
    department=models.CharField(max_length=20,default='')
    isDelete=models.BooleanField(default=False)
    class Meta:
        db_table='staffinfo'