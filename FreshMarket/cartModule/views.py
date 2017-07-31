from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from userModule.decorator_login import *
from cartModule.models import *


# Create your views here.
@login_checker
def cart_info(request):
    cart_list = CartInfo.objects.filter(user__userID=request.session['userId'])
    context = {'page_name': 1, 'title': '购物车', 'cart_list': cart_list}
    return render(request, 'cartModule/cart.html', context)


@login_checker
def add(request, gid, count):
    # 添加商品到数据库
    carts = CartInfo.objects.filter(goods_id=gid).filter(user__userID=request.session['userId'])
    if len(carts) == 0:
        cart = CartInfo()
        cart.goods_id = int(gid)
        cart.count = int(count)
        cart.user_id = request.session['userId']
    else:
        cart = carts[0]
        cart.count += int(count)
    cart.save()

    # 返回到页面
    if request.is_ajax():
        context = {'count': CartInfo.objects.filter(user__userID=request.session['userId']).count()}
        return JsonResponse(context)
    else:
        return redirect('/cart/')


# 更改商品的数量
def count_change(request):
    gid = request.GET.get('gid')
    count = request.GET.get('count')
    cart = CartInfo.objects.get(id=int(gid))
    print(cart.count)
    cart.count = int(count)
    cart.save()
    print(cart.count)
    return JsonResponse({'count': cart.count})


# 删除指定的购物车商品
def delete(request):
    id = request.GET.get('id')
    cart = CartInfo.objects.get(id=int(id))
    cart.delete()
    return JsonResponse({'result': 'ok'})