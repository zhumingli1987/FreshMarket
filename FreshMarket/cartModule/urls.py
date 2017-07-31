from django.conf.urls import url
from cartModule import views

urlpatterns = [
    url('^$', views.cart_info),
    url('^add(\d+)_(\d+)/$', views.add),
    url('^delete/$', views.delete),
    url('^count_change/', views.count_change)
]