from django.conf.urls import url
from orderModule import views

urlpatterns = [
    url('^$', views.order),
    url('^order_add/', views.order_add),
]