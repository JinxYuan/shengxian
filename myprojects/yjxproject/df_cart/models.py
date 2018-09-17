from django.db import models

class Cart(models.Model):
    goods = models.ForeignKey('df_goods.GoodsInfo')
    user = models.ForeignKey('shengxianapp.SXUser')
    count = models.IntegerField()
