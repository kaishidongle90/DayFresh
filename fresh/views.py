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
# 将数据类型传到html页面中，在html里处理
    goodstypelist = GoodsType.objects.all()
    dic['goodstypelist'] = goodstypelist
    return render(request,'fresh/index.html',dic)

def login(request):
    return render(request,'fresh/login.html')

#登陆页面的判断，验证用户的密码是否正确
def loginHandler(request):
    uname = request.POST['username']
    upwd = request.POST['pwd']
    #判断密码是否为空 ，不能使用get方法， 因为get方法得到的是一个对象，没有True和False之分
    # filter 得到的是一个列表，可以判断长度
    pwdtest = UserInfo.objects.filter(upwd=upwd)
    if len(pwdtest) == 0:
        return HttpResponse('passwd cannot be null')
    #判断用户名是否存在
    nametest = UserInfo.objects.filter(uname=uname)
    if len(nametest)>0 and len(pwdtest)>0:
    	request.session["username"] = uname
        return redirect('/index/')
    else:
 
        return HttpResponse('user or pwd is error ')


#@longin_test  判断用户是否存在，如果不存在，则跳到login页面，用在用户必须登陆的地方，像用户中心
@longin_test
#使用/login/写入的session ，可以在多个页面中使用
@transSession
def user_center_info(request,dic):
    userinfo = UserInfo.objects.get(uname=dic['username'])

    # -------------- zuijin liulan ----------
    goodslist = JustSaw.objects.order_by('-id')[0:5]
    sawlist = []
    for i in goodslist:
        id = int(i.jgoodsid)
        sawlist.append(GoodsInfo.objects.get(pk=id))

    # -------------- zuijin liulan ----------

    dic['phoneNum'] = userinfo.uphoneNum,
    dic['address'] = userinfo.uaddress
    dic['sawlist'] = sawlist
    return render(request,'fresh/user_center_info.html',dic)
@transSession
def user_center_site(request,dic):
    # dic['username'] 从seesion中取值
    userinfo = UserInfo.objects.get(uname=dic['username'])
    dic['phoneNum'] = userinfo.uphoneNum,
    dic['address'] = userinfo.uaddress,
    return render(request,'fresh/user_center_site.html',dic)

def register(request):
    return render(request,'fresh/register.html')

#对注册页的数据进行判断处理
def register_handle(request):
    uname = request.POST.get('user_name')
    # 如果用户名存在不能为空
    nametest = UserInfo.objects.filter(uname=uname)
    if len(uname)>8 and len(uname)<20 and len(nametest)==0:
        pass
    else:
        return HttpResponse('please pick another name')
    upwd = request.POST.get('pwd')
    if len(upwd)>=8 and len(upwd)<=20:
        pass
    else:
         return HttpResponse('the passwd must more than 8 less 20')
    ucpwd = request.POST.get('cpwd')
    if upwd != ucpwd:
        return HttpResponse('the passwd is different')
    uemail = request.POST.get('email')
    # 判断邮箱是否合法
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

#修改用户的地址 电话 邮编等
def reciver_handle(request):
    reciver = request.POST.get('reciver')
    address = request.POST.get('address')
    postcode = request.POST.get('postcode')
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

@transSession
def list(request,dic,typeId,pageNum):
    goods = GoodsType.objects.get(pk=typeId)
    goodstype = GoodsType.objects.get(pk=typeId)
    #按id顺序取出数据（正常排序）

    goodslist = goods.goodsinfo_set.order_by('id')
    sec = request.GET.get('sec')
    if sec=='desc':
        goodslist = goods.goodsinfo_set.order_by('-gprice')
        sec = 'desc'
    else:
        sec = 'asc'

    recommend = goods.goodsinfo_set.order_by('-id')[0:2]
    p = Paginator(goodslist,4)
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
    page = 'list'
    dic['goodstype'] = goodstype
    dic['typeId'] = typeId
    dic['goodslist'] = goodslist
    dic['prange'] = prange
    dic['list1'] = list1
    dic['recommend'] = recommend
    dic['prePageNum'] = prePageNum
    dic['nextPageNum'] = nextPageNum
    dic['sec'] = sec
    dic['page'] = page
    dic['pageNum'] = int(pageNum)
    return render(request,'fresh/list.html',dic)

@transSession
def listByPrice(request,dic,typeId,pageNum):
    goods = GoodsType.objects.get(pk=typeId)
    #按id顺序取出数据（正常排序）

    goodslist = goods.goodsinfo_set.order_by('gprice')
    sec = request.GET.get('sec')
    if sec=='desc':
        goodslist = goods.goodsinfo_set.order_by('-gprice')
        sec = 'desc'
    else:
        sec = 'asc'

    recommend = goods.goodsinfo_set.order_by('-id')[0:2]
    p = Paginator(goodslist,4)
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
    page = 'listByPrice'

    dic['typeId'] = typeId
    dic['goodslist'] = goodslist
    dic['prange'] = prange
    dic['list1'] = list1
    dic['recommend'] = recommend
    dic['prePageNum'] = prePageNum
    dic['nextPageNum'] = nextPageNum
    dic['sec'] = sec
    dic['page'] = page
    dic['pageNum'] = int(pageNum)
    return render(request, 'fresh/list.html', dic)

@transSession
def detail(request,dic,typeId,goodsId):
    justsaw = JustSaw()
    justsaw.jgoodsid = goodsId
    justsaw.save()

    goodsType = GoodsType.objects.get(pk=typeId)
    goods = goodsType.goodsinfo_set.get(pk=goodsId)
    recommend = goodsType.goodsinfo_set.order_by('-id')[0:2]
    dic['typeId'] = typeId
    dic['goods'] = goods
    dic['recommend'] = recommend
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
def add_cart(request, dic):
    id1 = request.GET['gid']
    num = request.GET['gnum']
    print id1, num
    user = UserInfo.objects.get(uname=dic['username'])
    goods = GoodsInfo.objects.get(pk=id1)
    print goods

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
    id = idlist[0]
    num = numlist[0]

    cart = CartInfo.objects.get(pk=id)
    cart.cnum = num
    cart.save()


@longin_test   
@transSession
def user_center_order(request,dic):
    user = UserInfo.objects.get(uname=dic['username'])
    orderlist = user.orderinfo_set.order_by('-id')
    dic['orderlist']=orderlist
    return render(request,'fresh/user_center_order.html',dic)



@longin_test
@transSession
def orderHandle(request,dic):
    data=request.POST
    numlist=data.getlist('nums[]')
    idlist=data.getlist('ids[]')
    totallist=data.getlist('totals[]')
    total=data.getlist('total[]')
    cartlist=data.getlist('cartidlist[]')
    print numlist,idlist,totallist,total,cartlist

    user = UserInfo.objects.get(uname=dic['username'])
    order = OrderInfo()
    order.ouser = user
    order.odate = datetime.now()
    order.ototalprice = total[0]
    order.ispay = True
    order.save()

    for i in range(len(idlist)):
        oDetail = OrderDetialInfo()
        oDetail.dorder = order
        oDetail.dgoods = GoodsInfo.objects.get(pk=idlist[i])
        oDetail.dnum = numlist[i]
        oDetail.dtotal = totallist[i]
        oDetail.save()
        cart=CartInfo.objects.get(pk=int(cartlist[i]))
        cart.delete()



    return redirect('/user_center_order/')



@longin_test
@transSession
def place_order1(request, dic):
    id1 = request.GET['gid']
    num = request.GET['gnum']
    print id1,num
    user = UserInfo.objects.get(uname=dic['username'])
    goods = GoodsInfo.objects.get(pk=id1)
    dic['user'] = user
    dic['goods'] = goods
    dic['num'] = num
    print dic

    return render(request, 'fresh/place_order1.html', dic)


# 根据register.js提交过来的数据 ，判断用户名是否存在 在register.html中
def check_name(request):
    # POST AND GET  方法都是可以的
    user=request.POST['username']
    if UserInfo.objects.get(uname=user):
        return HttpResponse('ok')