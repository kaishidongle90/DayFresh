#coding=utf-8
from django.db import models
#from __future__ import unicode_literals
from tinymce.models import HTMLField


#Table for user
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=30)
    uphoneNum = models.BigIntegerField(default=0,null=True,blank=True)
    uaddress = models.CharField(max_length=50,null=True,blank=True)
    uemail = models.EmailField()
    upostcode = models.IntegerField(default=0,null=True,blank=True)

    class Meta():
        db_table = 'userinfo'

    def __str__(self):
        return self.uname.encode('utf-8')

#Table for goods
class GoodsType(models.Model):
    ttitle = models.CharField(max_length=20)

    class Meta():
        db_table = 'goodstype'
    def __str__(self):
        return self.ttitle.encode('utf-8')


class GoodsInfo(models.Model):
    gname = models.CharField(max_length=20)
    gsubname = models.CharField(max_length=70)
    gdesc = HTMLField()
    geval = HTMLField(null=True, blank=True)
    gprice = models.DecimalField(max_digits=5, decimal_places=2)
    gunit = models.CharField(max_length=20)
    gpic = models.ImageField(upload_to='fresh/images/goods/')
    gpubdate = models.DateTimeField()
    gsales = models.IntegerField(default=0)
    gcounts = models.IntegerField(default=0)
    gtype = models.ForeignKey(GoodsType)

    class Meta():
        db_table = 'goodsinfo'

    def __str__(self):
        return self.gname.encode('utf-8')


# Table for cart 

class CartInfo(models.Model):
    cuser = models.ForeignKey('userInfo')

    cgoods = models.ForeignKey('goodsInfo')
    cbuy_date = models.DateTimeField()
    cnum = models.IntegerField(default=0)
    # isDelete = models.BooleanField(default=False)

    class Meta():
        db_table = 'cartInfo'
        ordering = ['id']

class OrderInfo(models.Model):
    ouser = models.ForeignKey('UserInfo')
    odate = models.DateTimeField()
    ototalprice = models.DecimalField(max_digits=6, decimal_places=2)
    ispay = models.BooleanField(default=False)

    class Meta():
        db_table = 'orderInfo'
        ordering = ['id']

    def __str__(self):
        return "%d" % self.pk


class OrderDetialInfo(models.Model):
    dorder = models.ForeignKey('OrderInfo')
    dgoods = models.ForeignKey('GoodsInfo')
    dnum = models.IntegerField(default=0)
    dtotal = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta():
        db_table = 'orderDetialInfo'
        ordering = ['id']
