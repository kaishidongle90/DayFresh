from django.contrib import admin
from models import *
# Register your models here.


class GoodsTypeAdmin(admin.ModelAdmin):
	list_display = ['id','ttitle']

class GoodsInfoAdmin(admin.ModelAdmin):
	list_display = ['id','gname','gprice','gpic','gdesc']

class UserInfoAdmin(admin.ModelAdmin):
	list_display = ['id','uname','upwd','uphoneNum','uaddress','uemail','upostcode']

class CartInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'cuser', 'cgoods','cnum','cbuy_date']



class OrderInfoAdmin(admin.ModelAdmin):
    list_display = ['id','ouser','ototalprice','ispay','odate']




class OrderDetialInfoAdmin(admin.ModelAdmin):
    list_display = ['id','dorder','dgoods','dnum','dtotal']


class JustSawAdmin(admin.ModelAdmin):
	list_display = ['id','jgoodsid']


admin.site.register(OrderDetialInfo, OrderDetialInfoAdmin)
admin.site.register(GoodsType,GoodsTypeAdmin)
admin.site.register(GoodsInfo,GoodsInfoAdmin)
admin.site.register(UserInfo,UserInfoAdmin)
admin.site.register(OrderInfo, OrderInfoAdmin)
admin.site.register(CartInfo, CartInfoAdmin)
admin.site.register(JustSaw, JustSawAdmin)