from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from goodsModule.models import *
from django.core.paginator import Paginator
from cartModule.models import CartInfo
from haystack.views import SearchView


# Create your views here.
def index(request):
    gtl = GoodsType.objects.all()
    dict_list = []
    for gtype in gtl:
        dict_list.append({
            'type': gtype,
            'list_a': gtype.goodsinfo_set.order_by('-goodsClick')[0:3],
            'list_b': gtype.goodsinfo_set.order_by('-id')[0:4]
        })
    context = {'title': '首页', 'list': dict_list, 'count': cart_count(request)}
    return render(request, 'goodsModule/index.html', context)


def goods_list(request, tid, oid, pid):
    # 查询商品的类型。
    gtype = GoodsType.objects.get(id=int(tid))
    # 查询指定分类的两种最新商品。
    new_glt = gtype.goodsinfo_set.order_by('-id')[0:2]
    # 查询指定分类的所有商品。
    # glt = gtype.goodsinfo_set.order_by('-id')
    glt = GoodsInfo.objects.filter(goodsType_id=int(tid))

    # 根据指定的规则进行分类。
    if oid == '3':
        glt = glt.order_by('-goodsClick')
    elif oid == '2':
        glt = glt.order_by('-goodsPrice')
    else:
        glt = glt.order_by('-id')

    # 进行分页
    paginator = Paginator(glt, 10)
    pdx = int(pid)
    if pdx == 0:
        pdx = 1
    elif pdx > paginator.num_pages:
        pdx = paginator.num_pages
    page = paginator.page(pdx)
    context = {'title': '商品列表', 'oid': oid, 'gtype': gtype, 'new_glt': new_glt, 'page': page, 'count': cart_count(request)}
    return render(request, 'goodsModule/list.html', context)


def goods_detail(request, gid):
    goods = GoodsInfo.objects.get(id=gid)
    # 更改商品的点击量
    goods.goodsClick += 1
    goods.save()
    # 查询当前类型的商品，取出最新的两中商品作为推荐商品。
    new_glt = goods.goodsType.goodsinfo_set.order_by('-id')[0:2]
    context = {'title': '商品详情', 'goods': goods, 'new_glt': new_glt, 'count': cart_count(request)}
    response = render(request, 'goodsModule/detail.html', context)

    # 最近浏览
    view_list = request.COOKIES.get('view_list', '')
    if view_list == '':
        response.set_cookie('view_list', gid)
    else:
        view_list = view_list.split(',')
        # 测试gid是否在list列表内，如果在，删除后重新插入，不在，就直接插入。
        if gid in view_list:
            view_list.remove(gid)
        view_list.insert(0, gid)

        # 保证只有5个元素
        if len(view_list) > 5:
            view_list.pop()
        view_list = ','.join(view_list)
        response.set_cookie('view_list', view_list)
    return response


def cart_count(request):
    if request.session.has_key('userId'):
        return CartInfo.objects.filter(user_id=request.session['userId']).count()
    else:
        return 0


class MySearch(SearchView):
    def extra_context(self):
        extra = super(MySearch, self).extra_context()
        extra['title'] = "搜索"
        extra['guest_cart'] = 1
        extra['cart_count'] = cart_count(self.request)
        return extra

