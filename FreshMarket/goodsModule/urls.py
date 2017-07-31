from django.conf.urls import url
from goodsModule import views


urlpatterns = [
    url('^$', views.index),
    url('^list(\d+)_(\d+)_(\d+)/$', views.goods_list),
    url('^(\d+)/$', views.goods_detail),
    url('^search/$', views.MySearch()),

]