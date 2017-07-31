from django.db import models


# Create your models here.
class OrderInfo(models.Model):
    # 订单编号=用户编号+下单时间
    order_id = models.CharField(max_length=20, primary_key=True)
    order_user = models.ForeignKey('userModule.UserInfo')
    order_date = models.DateField(auto_now_add=True)
    order_pay = models.BooleanField(default=False)
    order_total = models.DecimalField(max_digits=6, decimal_places=2)
    # 送货地址可能会变，需要记录送货地址。
    order_address = models.CharField(max_length=150)


class OrderDetailInfo(models.Model):
    order = models.ForeignKey(OrderInfo)
    goods = models.ForeignKey('goodsModule.GoodsInfo')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    count = models.IntegerField()


















