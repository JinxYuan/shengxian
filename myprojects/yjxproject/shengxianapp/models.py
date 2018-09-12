from django.db import models


class SXUser(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=40)
    uemail = models.CharField(max_length=30)
    ushouname = models.CharField(max_length=10, default='')
    uaddress = models.CharField(max_length=100, default='')
    uyoubian = models.CharField(max_length=6, default='')
    uphone = models.CharField(max_length=11, default='')
    isDelete = models.BooleanField(default=False)

