from django.db import models


# 创建用户模型类
class User(models.Model):
    userID = models.IntegerField('userId', primary_key=True, auto_created=True)
    userName = models.CharField('userName', max_length=20, null='false')
    password = models.CharField('password', max_length=40, null='false')
    email = models.CharField('email', max_length=40, null='false')
    telephone = models.CharField('telephone', max_length=20)

    class Meta:
        db_table = 'userTable'


class Address(models.Model):
    addressInfo = models.CharField('addressInfo', max_length=150)
    addressId = models.IntegerField('addressId')
    addressUser = models.ForeignKey('User')

    class Meta:
        db_table = 'addressTable'


class Order(models.Model):
    orderID = models.AutoField('orderId', primary_key=True, max_length=12)
    orderTime = models.DateTimeField('orderTime', auto_now_add=True)
    payInfo = models.BooleanField('payInfo', default='false')
    moneyCount = models.FloatField('moneyCount', )
    orderUser = models.ForeignKey('User')
    orderGoods = models.ManyToManyField('Goods')

    class Meta:
        db_table = 'orderTable'


class Goods(models.Model):

    class Meta:
        db_table = 'goodsTable'







