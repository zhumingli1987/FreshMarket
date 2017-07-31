from django.db import models
from goodsModule.models import GoodsInfo
from userModule.models import UserInfo


# Create your models here.
class CartInfo(models.Model):
    goods = models.ForeignKey(GoodsInfo)
    count = models.IntegerField()
    user = models.ForeignKey(UserInfo)
