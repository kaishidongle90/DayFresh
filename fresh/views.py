#coding=utf-8
from django.shortcuts import render,redirect
from django.http import *
from models import *
from datetime import datetime
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
import re
from transSession import transSession,longin_test
# Create your views here.

@transSession
def index(request,dic):
    fruitType = GoodsType.objects.get(pk=4)
    seafoodType = GoodsType.objects.get(pk=5)
    fruitlist = fruitType.goodsinfo_set.all()[0:4]
    seafoodlist = seafoodType.goodsinfo_set.all()[0:4]
    print seafoodlist,seafoodType
    dic['fruitlist'] = fruitlist
    dic['fruitTypeId'] = 4
    dic['seafoodlist'] = seafoodlist
    dic['seafoodTypeId'] = 5
    return render(request,'fresh/index.html',dic)


def login(request):
    return render(request,'fresh/login.html')


def loginHandler(request):
    uname = request.POST['username']
    upwd = request.POST['pwd']
    pwdtest = UserInfo.objects.filter(upwd=upwd)
    if len(pwdtest) == 0:
        return HttpResponse('passwd cannot be null')
    nametest = UserInfo.objects.filter(uname=uname)
    if len(nametest)>0 and len(pwdtest)>0:
    	request.session["username"] = uname
        return redirect('/index/')
    else:
        return HttpResponse('user or pwd is error ')
@longin_test
@transSession
def user_center_info(request,dic):
    userinfo = UserInfo.objects.get(uname=dic['username'])
    dic['phoneNum'] = userinfo.uphoneNum,
    dic['address'] = userinfo.uaddress
    return render(request,'fresh/user_center_info.html',dic)
@transSession
def user_center_site(request,dic):
    userinfo = UserInfo.objects.get(uname=dic['username'])
    dic['phoneNum'] = userinfo.uphoneNum,
    dic['address'] = userinfo.uaddress,
    return render(request,'fresh/user_center_site.html',dic)

def register(request):
    return render(request,'fresh/register.html')

def register_handle(request):
    uname = request.POST.get('user_name')
    nametest = UserInfo.objects.filter(uname=uname)
    if len(uname)>5 and len(uname)<20 and len(nametest)==0:
        pass
    else:
        return HttpResponse('please pick another name')
    upwd = request.POST.get('pwd')
    if len(upwd)>=5 and len(upwd)<=20:
        pass
    else:
         return HttpResponse('the passwd must more than 8 less 20')
    ucpwd = request.POST.get('cpwd')
    if upwd != ucpwd:
        return HttpResponse('the passwd is different')
    uemail = request.POST.get('email')
 
    isMatch = bool(re.match('[a-zA-Z0-9][\w]{0,19}@[a-zA-Z0-9]{2,6}\.(com|cn)$', uemail,re.VERBOSE));  
    if not isMatch:  
        return HttpResponse('please write the right email') 


    print uname,upwd,uemail
    u = UserInfo()
    u.uname = uname
    u.upwd = upwd
    u.uemail = uemail
    u.save()
#    users.cu.create_user(uname,upwd,uemail)
    return redirect('/login/')




@longin_test
@transSession
def place_order(request,dic):
    user = UserInfo.objects.get(uname=dic['username'])
    dic['user'] = user
    dic1 = request.POST
    idlist = dic1.getlist('cart_id')
    cartlist = []
    for id in idlist:
        cart = CartInfo.objects.get(pk=id)
        cartlist.append(cart)
    dic['cartlist']=cartlist




    return render(request,'fresh/place_order.html',dic)


def reciver_handle(request):
    reciver = request.POST.get('reciver')
    address = request.POST.get('address')
    postcode = request.POST.get('postcode')
    print reciver
    phoneNum = request.POST.get('phoneNum')
    u = UserInfo.objects.get(uname=reciver)
    u.uaddress = address
    u.upostcode = postcode
    u.uphoneNum = phoneNum
    u.save()
    return HttpResponse('ok')


def exit(request):
 	del request.session['username']
 	return redirect('/index/')


def list(request,typeId,pageNum):
    fruit = GoodsType.objects.get(pk=typeId)
    #按id顺序取出数据（正常排序）
    fruitlist = fruit.goodsinfo_set.all()
    #按价格倒序取出数据
    ivertedfruitlist = fruit.goodsinfo_set.order_by('-gprice')
    #按价格正序取出数据
    positivefruitlist = fruit.goodsinfo_set.order_by('-gprice')
    #推荐商品取值
    recommend = fruit.goodsinfo_set.order_by('-id')[0:2]
    #分页
    # if priceId =='' or priceId == 1:
    #     fruitlist = normalfruitlist
    # else:
    #     fruitlist = ivertedfruitlist

    p = Paginator(fruitlist,4)
    if pageNum == '' :
        pageNum = 1

   
    prange = p.page_range
    #上一页功能实现
    if int(pageNum) > 1:
        prePageNum = int(pageNum) -1
    else:
        prePageNum = 1

    #下一页功能实现
    if int(pageNum) < p.num_pages:
        print type(pageNum)
        nextPageNum = int(pageNum) + 1
    else:
        nextPageNum = p.num_pages

    list1 = p.page(pageNum)
    dic = {
    # id is the fruitType's id , put id to list.html for zhanweifu, nothing speical
            'typeId':typeId,
            'fruitlist':fruitlist,
            'prange': prange,
            'list1':list1,
            'recommend':recommend,
            'prePageNum':prePageNum,
            'nextPageNum':nextPageNum,
    }
    return render(request,'fresh/list.html',dic)



def detail(request,typeId,goodsId):
    goodsType = GoodsType.objects.get(pk=typeId)
    goods = goodsType.goodsinfo_set.get(pk=goodsId)
    recommend = goodsType.goodsinfo_set.order_by('-id')[0:2]
    dic = {
        'typeId':typeId,
        'goods':goods,
        'recommend':recommend,
    }
    return render(request,'fresh/detail.html',dic)

@longin_test
@transSession
def cart(request,dic):
    user = UserInfo.objects.get(uname = dic['username'])
    cartlist = user.cartinfo_set.all()
    # num = user.cartinfo_set.get('cnum')
    # print num
    dic['cart'] = cartlist
    return render(request, 'fresh/cart.html', dic)
@longin_test   
@transSession
def add_cart(request,dic):
    id1 = request.GET['gid']
    num = request.GET['gnum']
    print id1,num
    user = UserInfo.objects.get(uname = dic['username'])
    goods = GoodsInfo.objects.get(pk=id1)

    if CartInfo.objects.filter(cgoods=goods):
        cart = CartInfo.objects.get(cgoods=goods)
        cart.cnum += int(num)
        cart.save()
    else:
        cart = CartInfo()         
        cart.cuser = user
        cart.cgoods = goods
        cart.cbuy_date = datetime.now()
        cart.cnum = num
        cart.save()
    return redirect('/cart/')
def del_cart(request, id):
    cart = CartInfo.objects.get(pk=id)
    cart.delete()
    return redirect('/cart/')


def set_num(request):
    dic1 = request.POST
    numlist = dic1.getlist('num')
    idlist = dic1.getlist('id')
    for id in idlist:
        id=int(id)
    for num in numlist:
        num = int(num) 

    cart = CartInfo.objects.get(pk=id)
    cart.cnum = num
    cart.save()


@longin_test   
@transSession
def user_center_order(request,dic):
    user = UserInfo.objects.get(uname=dic['username'])
    orderlist = user.orderinfo_set.all()
    dic['orderlist']=orderlist
    return render(request,'fresh/user_center_order.html',dic)

# @longin_test   
# @transSession
# def orderHandle(request,dic):
#     user = UserInfo.objects.get(uname=dic['username'])
#     totalPrice = 
    
#     order = OrderInfo()
#     order.ouser = user
#     order.odate = datetime.now()
#     order.ototalprice = totalPrice
#     order.ispay = True
#     order.save()

#     idlist = []
#     numlist = []
#     dtotal = []
#     for i in range(len(goodslist):
#         oDetail = OrderDetialInfo()
#         oDetail.dorder = order
#         oDetail.dgoods = GoodsInfo.objects.get(pk=idlist[i])
#         oDetail.dnum = numlist[i]
#         oDetail.dtotal = dtotal[i]
#         oDetail.save()