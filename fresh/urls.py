from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$',views.index,name='index'),
    url(r'^index/$',views.index,name='index'),  
    url(r'^login/$',views.login,name='login'),
    url(r'^loginHandler/$',views.loginHandler,name='loginhandler'),  
    url(r'^user_center_info/$',views.user_center_info,name='user_center_info'),
    url(r'^user_center_site/$',views.user_center_site,name='user_center_site'),
    url(r'^register/$',views.register,name='register'),
    url(r'^register_handle/$',views.register_handle,name='register_handle'),

    url(r'^cart/$',views.cart,name='cart'),
    url(r'^place_order/$',views.place_order,name='place_order'),
    url(r'^place_order1/$',views.place_order1,name='place_order1'),
    url(r'^reciver_handle/$',views.reciver_handle,name='reciver_handle'), 
    url(r'^exit/$',views.exit,name='exit'), 
    url(r'^list([0-9]*)_([0-9]*)/$',views.list,name='list'),
    url(r'^listByPrice([0-9]*)_([0-9]*)/$',views.listByPrice,name='listByPrice'),
    url(r'^detail([0-9]*)_([0-9]*)/$',views.detail,name='detail'),
    url(r'^del_cart(?P<id>[0-9]+)/$',views.del_cart,name='del_cart'),
    url(r'^add_cart/$',views.add_cart,name='add_cart'),
    url(r'^user_center_order/$',views.user_center_order,name='user_center_order'),
    url(r'^orderHandle/$',views.orderHandle,name='orderHandle'),
    url(r'check_name/$',views.check_name,name='check_name'),
]
