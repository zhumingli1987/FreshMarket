from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class GoodsType(models.Model):
    typeTitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.typeTitle.encode('utf-8')

    class Meta:
        db_table = 'tableGoodsType'


class GoodsInfo(models.Model):
    goodsTitle = models.CharField(max_length=20)
    goodsIntro = models.CharField(max_length=200)
    goodsPic = models.ImageField(upload_to='goods')
    goodsPrice = models.DecimalField(max_digits=6, decimal_places=2)
    goodsUnit = models.CharField(max_length=20, default='500g')
    goodsClick = models.IntegerField()
    goodsStock = models.IntegerField()
    goodsContent = HTMLField()
    goodsType = models.ForeignKey(GoodsType)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.goodsTitle.encode('utf-8')

    class Meta:
        db_table = 'tableGoodsInfo'
