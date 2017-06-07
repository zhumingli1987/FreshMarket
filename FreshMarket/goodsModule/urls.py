from django.conf.urls import url
from goodsModule import views


urlpatterns = [
    url('^$', views.index),
    url('index/$', views.index),

]