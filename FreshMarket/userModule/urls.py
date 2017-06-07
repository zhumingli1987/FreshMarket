from django.conf.urls import url
from userModule import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^register_handle/$', views.register_handle),
    url(r'^register_exist/$', views.register_exist),
    url(r'^login/$', views.login),
    url(r'^login_handle/$', views.login_handle),
    url(r'^logout/$', views.logout),
    url(r'^center_info', views.user_center),
    url(r'^center_order', views.user_order),
    url(r'^center_site', views.user_site),

]
