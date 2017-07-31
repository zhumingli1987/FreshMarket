from django.shortcuts import render, redirect
from django.http import HttpResponse
from userModule.models import *
from cartModule.models import *
from orderModule.models import *
from django.db import transaction
from datetime import datetime


# Create your views here.
def order(request):
    # 查询邮寄地址信息
    user = UserInfo.users.get(userID=request.session['userId'])
    add = Address.adds.get(addToUser=user)
    # 查询提交商品信息
    cart_ids = request.GET.getlist('cart_ids')
    carts = CartInfo.objects.filter(id__in=cart_ids)
    context = {'title': '订单提交', 'page_name': 1, 'address': add, 'carts': carts}
    return render(request, 'orderModule/place_order.html', context)


@transaction.atomic
def order_add(request):
    """ 订单提交保存 """
    post = request.POST
    address = post.get('address')
    cart_ids = post.getlist('cart_ids')
    print(cart_ids)

    # 设置保存点
    tid = transaction.savepoint()

    try:
        # 1、创建订单对象
        od = OrderInfo()
        now = datetime.now()
        uid = request.session['userId']
        total = 0
        od.order_id = '%d%s' % (uid, now.strftime('%Y%m%d%H%M%S'))
        od.order_user_id = uid
        od.order_date = now
        od.order_address = address
        od.order_total = total
        od.save()
        # 2、判断库存
        for cid in cart_ids:
            cart = CartInfo.objects.get(pk=cid)
            if cart.goods.goodsStorage >= cart.count:
                # 3、库存够卖，减少库存
                cart.goods.goodsStorage -= cart.count
                cart.goods.save()
                # 4、创建详单对象
                odi = OrderDetailInfo()
                odi.order = od
                odi.goods = cart.goods
                odi.price = cart.goods.goodsPrice
                odi.count = cart.count
                odi.save()
                total += cart.goods.goodsPrice*cart.count
                # 5、删除购物车数据
                cart.delete()
            else:
                # 库存不足，终止购买。
                transaction.savepoint_commit(tid)
                return redirect('/cart/')
        # 总计金额保存到订单
        od.order_total = total
        od.save()
        transaction.savepoint_commit(tid)
        # return render(request, '/user/center_order/')
    except Exception as e:
        # 事务回滚
        print('=============%s' % e)
        transaction.savepoint_rollback(tid)
    return redirect('/user/center_order/')








