from django.conf.urls import url
from userModule import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
    url(r'^user/register_handle/$', views.register_handle),
    url(r'^user/register_exit/', views.register_exist)
]